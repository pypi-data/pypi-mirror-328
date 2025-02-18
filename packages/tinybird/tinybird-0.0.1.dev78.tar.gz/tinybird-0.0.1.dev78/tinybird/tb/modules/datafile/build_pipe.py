import json
from copy import deepcopy
from typing import Any, Dict, List, Optional, Set
from urllib.parse import urlencode

import click
import requests
from croniter import croniter

from tinybird.client import DoesNotExistException, TinyB
from tinybird.tb.modules.common import requests_delete, requests_get
from tinybird.tb.modules.config import CLIConfig
from tinybird.tb.modules.datafile.common import ON_DEMAND, CopyModes, CopyParameters, PipeNodeTypes, PipeTypes
from tinybird.tb.modules.exceptions import CLIPipeException
from tinybird.tb.modules.feedback_manager import FeedbackManager


async def new_pipe(
    p,
    tb_client: TinyB,
    force: bool = False,
    check: bool = True,
    populate: bool = False,
    populate_subset=None,
    populate_condition=None,
    unlink_on_populate_error: bool = False,
    wait_populate: bool = False,
    skip_tokens: bool = False,
    ignore_sql_errors: bool = False,
    only_response_times: bool = False,
    run_tests: bool = False,
    as_standard: bool = False,
    tests_to_run: int = 0,
    tests_relative_change: float = 0.01,
    tests_to_sample_by_params: int = 0,
    tests_filter_by: Optional[List[str]] = None,
    tests_failfast: bool = False,
    tests_ignore_order: bool = False,
    tests_validate_processed_bytes: bool = False,
    override_datasource: bool = False,
    tests_check_requests_from_branch: bool = False,
    config: Any = None,
    fork_downstream: Optional[bool] = False,
    fork: Optional[bool] = False,
):
    # TODO use tb_client instead of calling the urls directly.
    host = tb_client.host
    config = CLIConfig().get_project_config()
    token = config.get_user_token()

    headers = {"Authorization": f"Bearer {token}"}

    cli_params = {}
    cli_params["cli_version"] = tb_client.version
    cli_params["description"] = p.get("description", "")
    cli_params["ignore_sql_errors"] = "true" if ignore_sql_errors else "false"
    cli_params["workspace_id"] = config.get("id", None)

    r: requests.Response = await requests_get(f"{host}/v0/playgrounds?{urlencode(cli_params)}", headers=headers)
    current_pipe = None
    pipe_exists = False
    playgrounds_response = r.json() if r.status_code == 200 else None
    if playgrounds_response:
        playgrounds = playgrounds_response["playgrounds"]
        current_pipe = next((play for play in playgrounds if play["name"] == p["name"] + "__tb__playground"), None)
        pipe_exists = current_pipe is not None

    for node in p["nodes"]:
        if node["params"]["name"] == p["name"]:
            raise click.ClickException(FeedbackManager.error_pipe_node_same_name(name=p["name"]))

    params = {}
    params.update(cli_params)
    if force:
        params["force"] = "true"
    if populate:
        params["populate"] = "true"
    if populate_condition:
        params["populate_condition"] = populate_condition
    if populate_subset:
        params["populate_subset"] = populate_subset
    params["unlink_on_populate_error"] = "true" if unlink_on_populate_error else "false"
    params["branch_mode"] = "fork" if fork_downstream or fork else "None"

    body = {"name": p["name"], "description": p.get("description", "")}

    def parse_node(node):
        if "params" in node:
            node.update(node["params"])
            if node.get("type", "") == "materialized" and override_datasource:
                node["override_datasource"] = "true"
            del node["params"]
        return node

    if p["nodes"]:
        body["nodes"] = [parse_node(n) for n in p["nodes"]]

    post_headers = {"Content-Type": "application/json"}

    post_headers.update(headers)

    try:
        user_client = deepcopy(tb_client)
        config = CLIConfig().get_project_config()
        user_client.token = config.get_user_token()
        params["workspace_id"] = config.get("id", None)
        body["name"] = p["name"] + "__tb__playground"

        if pipe_exists and current_pipe:
            data = await user_client._req(
                f"/v0/playgrounds/{current_pipe['id']}?{urlencode(params)}",
                method="PUT",
                headers=post_headers,
                data=json.dumps(body),
            )

        else:
            data = await user_client._req(
                f"/v0/playgrounds?{urlencode(params)}",
                method="POST",
                headers=post_headers,
                data=json.dumps(body),
            )
    except Exception as e:
        raise click.ClickException(FeedbackManager.error_pushing_pipe(pipe=p["name"], error=str(e)))

    if p["tokens"] and not skip_tokens and not as_standard and data.get("type") in ["endpoint", "copy"]:
        # search for token with specified name and adds it if not found or adds permissions to it
        t = None
        for tk in p["tokens"]:
            token_name = tk["token_name"]
            t = await tb_client.get_token_by_name(token_name)
            if t:
                scopes = [f"PIPES:{tk['permissions']}:{p['name']}"]
                for x in t["scopes"]:
                    sc = x["type"] if "resource" not in x else f"{x['type']}:{x['resource']}"
                    scopes.append(sc)
                try:
                    r = await tb_client.alter_tokens(token_name, scopes)
                    token = r["token"]  # type: ignore
                except Exception as e:
                    raise click.ClickException(FeedbackManager.error_creating_pipe(error=e))
            else:
                token_name = tk["token_name"]
                try:
                    r = await tb_client.create_token(
                        token_name, [f"PIPES:{tk['permissions']}:{p['name']}"], "P", p["name"]
                    )
                    token = r["token"]  # type: ignore
                except Exception as e:
                    raise click.ClickException(FeedbackManager.error_creating_pipe(error=e))

    if data.get("type") == "endpoint":
        token = tb_client.token
        try:
            example_params = {
                "format": "json",
                "pipe": p["name"],
                "q": "",
                "token": token,
            }
            endpoint_url = await tb_client._req(f"/examples/query.http?{urlencode(example_params)}")
            if endpoint_url:
                endpoint_url = endpoint_url.replace("http://localhost:8001", host)
                click.echo(f"""** => Test endpoint with:\n** $ curl {endpoint_url}""")
        except Exception:
            pass


async def get_token_from_main_branch(branch_tb_client: TinyB) -> Optional[str]:
    token_from_main_branch = None
    current_workspace = await branch_tb_client.workspace_info()
    # current workspace is a branch
    if current_workspace.get("main"):
        response = await branch_tb_client.user_workspaces()
        workspaces = response["workspaces"]
        prod_workspace = next(
            (workspace for workspace in workspaces if workspace["id"] == current_workspace["main"]), None
        )
        if prod_workspace:
            token_from_main_branch = prod_workspace.get("token")
    return token_from_main_branch


async def check_materialized(pipe, host, token, cl, override_datasource=False, current_pipe=None):
    checker_pipe = deepcopy(pipe)
    checker_pipe["name"] = f"{checker_pipe['name']}__checker"
    headers = {"Authorization": f"Bearer {token}"}

    if current_pipe:
        from_copy_to_materialized = current_pipe["type"] == "copy"
        if from_copy_to_materialized:
            await cl.pipe_remove_copy(current_pipe["id"], current_pipe["copy_node"])

    materialized_node = None
    for node in checker_pipe["nodes"]:
        if node["params"]["type"] == "materialized":
            materialized_node = deepcopy(node)
            materialized_node["params"]["override_datasource"] = "true" if override_datasource else "false"
        node["params"]["type"] = "standard"

    try:
        pipe_created = False
        await new_pipe(
            checker_pipe, cl, force=True, check=False, populate=False, skip_tokens=True, ignore_sql_errors=False
        )
        pipe_created = True
        response = await cl.analyze_pipe_node(checker_pipe["name"], materialized_node, dry_run="true")
        if response.get("warnings"):
            show_materialized_view_warnings(response["warnings"])

    except Exception as e:
        raise click.ClickException(FeedbackManager.error_while_check_materialized(error=str(e)))
    finally:
        if pipe_created:
            r = await requests_delete(f"{host}/v0/pipes/{checker_pipe['name']}", headers=headers)
            if r.status_code != 204:
                click.echo(FeedbackManager.warning_check_pipe(content=r.content))


async def check_copy_pipe(pipe, copy_node, tb_client: TinyB):
    target_datasource = copy_node["params"].get("target_datasource", None)
    if not target_datasource:
        raise CLIPipeException(FeedbackManager.error_creating_copy_pipe_target_datasource_required())

    try:
        await tb_client.get_datasource(target_datasource)
    except DoesNotExistException:
        raise CLIPipeException(
            FeedbackManager.error_creating_copy_pipe_target_datasource_not_found(target_datasource=target_datasource)
        )
    except Exception as e:
        raise CLIPipeException(FeedbackManager.error_exception(error=e))

    schedule_cron = copy_node["params"].get(CopyParameters.COPY_SCHEDULE, None)
    is_valid_cron = not schedule_cron or (
        schedule_cron and (schedule_cron == ON_DEMAND or croniter.is_valid(schedule_cron))
    )

    if not is_valid_cron:
        raise CLIPipeException(FeedbackManager.error_creating_copy_pipe_invalid_cron(schedule_cron=schedule_cron))

    mode = copy_node["params"].get("mode", CopyModes.APPEND)
    is_valid_mode = CopyModes.is_valid(mode)

    if not is_valid_mode:
        raise CLIPipeException(FeedbackManager.error_creating_copy_pipe_invalid_mode(mode=mode))

    if not pipe:
        return

    pipe_name = pipe["name"]
    pipe_type = pipe["type"]

    if pipe_type == PipeTypes.ENDPOINT:
        await tb_client.pipe_remove_endpoint(pipe_name, pipe["endpoint"])

    if pipe_type == PipeTypes.DATA_SINK:
        await tb_client.pipe_remove_sink(pipe_name, pipe["sink_node"])

    if pipe_type == PipeTypes.STREAM:
        await tb_client.pipe_remove_stream(pipe_name, pipe["stream_node"])


async def check_sink_pipe(pipe, sink_node, tb_client: TinyB):
    if not sink_node["export_params"]:
        return

    if not pipe:
        return

    pipe_name = pipe["name"]
    pipe_type = pipe["type"]

    schedule_cron = sink_node["export_params"].get("schedule_cron", "")
    is_valid_cron = not schedule_cron or (schedule_cron and croniter.is_valid(schedule_cron))

    if not is_valid_cron:
        raise CLIPipeException(FeedbackManager.error_creating_sink_pipe_invalid_cron(schedule_cron=schedule_cron))

    if pipe_type == PipeTypes.ENDPOINT:
        await tb_client.pipe_remove_endpoint(pipe_name, pipe["endpoint"])

    if pipe_type == PipeTypes.COPY:
        await tb_client.pipe_remove_copy(pipe_name, pipe["copy_node"])

    if pipe_type == PipeTypes.STREAM:
        await tb_client.pipe_remove_stream(pipe_name, pipe["stream_node"])


async def check_stream_pipe(pipe, stream_node, tb_client: TinyB):
    if not stream_node["params"]:
        return

    if not pipe:
        return

    pipe_name = pipe["name"]
    pipe_type = pipe["type"]

    if pipe_type == PipeTypes.ENDPOINT:
        await tb_client.pipe_remove_endpoint(pipe_name, pipe["endpoint"])

    if pipe_type == PipeTypes.COPY:
        await tb_client.pipe_remove_copy(pipe_name, pipe["copy_node"])

    if pipe_type == PipeTypes.DATA_SINK:
        await tb_client.pipe_remove_sink(pipe_name, pipe["sink_node"])


def show_materialized_view_warnings(warnings):
    """
    >>> show_materialized_view_warnings([{'code': 'SIM', 'weight': 1}])

    >>> show_materialized_view_warnings([{'code': 'SIM', 'weight': 1}, {'code': 'HUGE_JOIN', 'weight': 2}, {'text': "Column 'number' is present in the GROUP BY but not in the SELECT clause. This might indicate a not valid Materialized View, please make sure you aggregate and GROUP BY in the topmost query.", 'code': 'GROUP_BY', 'weight': 100, 'documentation': 'https://tinybird.co/docs/guides/materialized-views.html#use-the-same-alias-in-select-and-group-by'}])
    ⚠️  Column 'number' is present in the GROUP BY but not in the SELECT clause. This might indicate a not valid Materialized View, please make sure you aggregate and GROUP BY in the topmost query. For more information read https://tinybird.co/docs/guides/materialized-views.html#use-the-same-alias-in-select-and-group-by or contact us at support@tinybird.co
    >>> show_materialized_view_warnings([{'code': 'SINGLE_JOIN', 'weight': 300}, {'text': "Column 'number' is present in the GROUP BY but not in the SELECT clause. This might indicate a not valid Materialized View, please make sure you aggregate and GROUP BY in the topmost query.", 'code': 'GROUP_BY', 'weight': 100, 'documentation': 'https://tinybird.co/docs/guides/materialized-views.html#use-the-same-alias-in-select-and-group-by'}])
    ⚠️  Column 'number' is present in the GROUP BY but not in the SELECT clause. This might indicate a not valid Materialized View, please make sure you aggregate and GROUP BY in the topmost query. For more information read https://tinybird.co/docs/guides/materialized-views.html#use-the-same-alias-in-select-and-group-by or contact us at support@tinybird.co
    """
    excluded_warnings = ["SIM", "SIM_UNKNOWN", "HUGE_JOIN"]
    sorted_warnings = sorted(warnings, key=lambda warning: warning["weight"])
    most_important_warning = {}
    for warning in sorted_warnings:
        if warning.get("code") and warning["code"] not in excluded_warnings:
            most_important_warning = warning
            break
    if most_important_warning:
        click.echo(
            FeedbackManager.single_warning_materialized_pipe(
                content=most_important_warning["text"], docs_url=most_important_warning["documentation"]
            )
        )


def is_endpoint_with_no_dependencies(
    resource: Dict[str, Any], dep_map: Dict[str, Set[str]], to_run: Dict[str, Dict[str, Any]]
) -> bool:
    if not resource or resource.get("resource") == "datasources":
        return False

    for node in resource.get("nodes", []):
        # FIXME: https://gitlab.com/tinybird/analytics/-/issues/2391
        if node.get("params", {}).get("type", "").lower() in [
            PipeNodeTypes.MATERIALIZED,
            PipeNodeTypes.COPY,
            PipeNodeTypes.DATA_SINK,
            PipeNodeTypes.STREAM,
        ]:
            return False

    for key, values in dep_map.items():
        if resource["resource_name"] in values:
            r = to_run.get(key, None)
            if not r:
                continue
            return False

    deps = dep_map.get(resource["resource_name"])
    if not deps:
        return True

    for dep in deps:
        r = to_run.get(dep, None)
        if is_endpoint(r) or is_materialized(r):
            return False

    return True


def is_endpoint(resource: Optional[Dict[str, Any]]) -> bool:
    if not resource:
        return False
    if resource.get("resource") != "pipes":
        return False

    if len(resource.get("tokens", [])) != 0:
        return True

    if any(node.get("params", {}).get("type", None) == "endpoint" for node in resource.get("nodes", [])):
        return True

    return False


def is_materialized(resource: Optional[Dict[str, Any]]) -> bool:
    if not resource:
        return False

    is_materialized = any(
        [node.get("params", {}).get("type", None) == "materialized" for node in resource.get("nodes", []) or []]
    )
    return is_materialized


def get_target_materialized_data_source_name(resource: Optional[Dict[str, Any]]) -> Optional[str]:
    if not resource:
        return None

    for node in resource.get("nodes", []):
        # FIXME: https://gitlab.com/tinybird/analytics/-/issues/2391
        if node.get("params", {}).get("type", "").lower() == PipeNodeTypes.MATERIALIZED:
            return node.get("params")["datasource"].split("__v")[0]

    return None
