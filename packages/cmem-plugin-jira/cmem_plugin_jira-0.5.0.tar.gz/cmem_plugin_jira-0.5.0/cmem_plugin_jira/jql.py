"""Jira JQL plugin module"""

import json
from collections.abc import Sequence
from tempfile import NamedTemporaryFile

from cmem_plugin_base.dataintegration.context import ExecutionContext, ExecutionReport
from cmem_plugin_base.dataintegration.description import Icon, Plugin, PluginParameter
from cmem_plugin_base.dataintegration.entity import (
    Entities,
)
from cmem_plugin_base.dataintegration.parameter.password import (
    Password,
    PasswordParameterType,
)
from cmem_plugin_base.dataintegration.plugins import WorkflowPlugin
from cmem_plugin_base.dataintegration.ports import FixedNumberOfInputs, FixedSchemaPort
from cmem_plugin_base.dataintegration.typed_entities.file import FileEntitySchema, LocalFile
from cmem_plugin_base.dataintegration.types import IntParameterType
from requests import request
from requests.auth import HTTPBasicAuth


@Plugin(
    label="JQL query",
    description="Search and retrieve JIRA issues.",
    documentation="""This plugin sends a [JQL query](https://www.atlassian.com/software/jira/guides/jql/overview)
to the [REST API (v2)](https://developer.atlassian.com/cloud/jira/platform/rest/v2/) of a given
JIRA Service.

The result is a list of JIRA issue descriptions.
This list is then bulk forwarded as a JSON document to the output port
(where you should connect a JSON Dataset).

This plugin is tested both with on-premise Jira deployments as well as with SAAS instances on
`atlassian.net`. Note that you need to create an API token for your Atlassian account,
to access the API of your atlassian.net hosted Jira instance.
""",
    icon=Icon(file_name="jira.svg", package=__package__),
    parameters=[
        PluginParameter(
            name="base_url",
            label="Jira Server",
            description="Base URL of the jira service, e.g. 'https://jira.example.org'",
            default_value="",
        ),
        PluginParameter(
            name="username",
            label="Account",
            default_value="",
        ),
        PluginParameter(
            name="password",
            label="Password or Token",
            param_type=PasswordParameterType(),
            default_value="",
        ),
        PluginParameter(
            name="jql_query",
            label="JQL Query",
            description="Warning: An empty query string retrieves all issues.",
            default_value="",
        ),
        PluginParameter(
            name="limit",
            label="Limit",
            description="Maximum number of issues to retrieve (0 = retrieve all issues).",
            param_type=IntParameterType(),
            default_value=0,
        ),
        PluginParameter(
            name="ssl_verify",
            label="Verify SSL Connection",
            advanced=True,
        ),
        PluginParameter(
            name="timeout",
            label="Connection Timeout",
            description="Number of seconds, the plugin will wait to "
            "establish a connection to the Jira Service.",
            advanced=True,
        ),
        PluginParameter(
            name="max_results",
            label="Results per Page",
            description="Number of items to return per request.",
            advanced=True,
        ),
    ],
)
class JqlQuery(WorkflowPlugin):
    """JQL Query Workflow Plugin"""

    def __init__(  # noqa: PLR0913
        self,
        base_url: str,
        username: str,
        password: Password | str,
        jql_query: str,
        limit: int = 0,
        ssl_verify: bool = True,
        timeout: int = 300,
        max_results: int = 100,
    ) -> None:
        self.base_url = base_url
        self.username = username
        self.password = password if isinstance(password, str) else password.decrypt()
        self.jql_query = jql_query
        if limit < 0:
            raise ValueError("Value of 'limit' must not be negative.")
        self.limit = limit
        self.ssl_verify = ssl_verify
        if timeout < 0:
            raise ValueError("Value of 'timeout' must not be negative.")
        self.timeout = timeout
        self.max_results = max_results
        self.input_ports = FixedNumberOfInputs([])
        self.output_port = FixedSchemaPort(schema=FileEntitySchema())

    def get_issues(self, context: ExecutionContext | None = None) -> list:
        """Do the GET requests to fetch all issues until the end.

        More details on the used API here:
        https://developer.atlassian.com/cloud/jira/platform/rest/v2/intro/
        """
        params: dict = {"jql": self.jql_query, "maxResults": self.max_results}
        issues: list[dict] = []
        finished = False
        while not finished:
            self.log.info(f"Start fetching max. {self.max_results} issues.")
            params["startAt"] = len(issues)
            response = request(
                "GET",
                f"{self.base_url}/rest/api/2/search",
                headers={"Accept": "application/json"},
                auth=HTTPBasicAuth(self.username, self.password),
                params=params,
                verify=self.ssl_verify,
                timeout=self.timeout,
            )
            response.raise_for_status()
            _ = json.loads(response.text)
            issues.extend(_["issues"])
            total = int(_["total"])
            left = total - len(issues)
            if 0 < self.limit < len(issues):
                issues = issues[: self.limit]
                self.log.info(f"Reached limit of {len(issues)} issues. That's all.")
                finished = True
            elif len(issues) >= _["total"]:
                self.log.info(f"Got {len(issues)} issues overall. That's all.")
                finished = True
            else:
                self.log.info(f"Got {len(issues)} issues. Still {left} left.")
            if context is not None:
                context.report.update(
                    ExecutionReport(
                        entity_count=len(issues),
                        operation="read",
                        operation_desc="issues imported",
                    )
                )

        return issues

    @staticmethod
    def dump_issues(issues: list) -> str:
        """Dump issues to file and return file name"""
        with NamedTemporaryFile(mode="w+", delete=False) as tmp_file:
            json.dump(issues, tmp_file, indent=2)
        return tmp_file.name

    def execute(self, inputs: Sequence[Entities], context: ExecutionContext) -> Entities:  # noqa: ARG002
        """Execute the workflow plugin on a given collection of entities"""
        self.log.info(f"Start executing JQL query: {self.jql_query}")
        context.report.update(
            ExecutionReport(entity_count=0, operation="read", operation_desc="issues retrieved")
        )
        issues = self.get_issues(context=context)
        schema = FileEntitySchema()
        file = self.dump_issues(issues)
        entities = [schema.to_entity(LocalFile(file, mime="application/json"))]
        self.log.info(f"Return File Entity: {file}")
        return Entities(entities=iter(entities), schema=FileEntitySchema())
