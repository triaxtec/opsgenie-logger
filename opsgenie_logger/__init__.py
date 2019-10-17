""" Provides logging handlers for OpsGenie """
import logging
from traceback import extract_tb, FrameSummary

from typing import Union

import opsgenie_sdk

__version__ = "0.1.4"


class OpsGenieHandler(logging.Handler):
    """
    A logging handler which pipes logs to OpsGenie

    When logging, the following OpsGenie fields are populated:
    message: log message
    alias: path:function:lineno
    description: exception info (if any)
    visible to: team name provided in __init__
    priority: Critical, error and warning are P1-3.  All others are P5
    """

    def __init__(self, api_key: str, team_name: str, level: Union[int, str] = logging.NOTSET):
        """
        :param api_key:  Your OpsGenie API key, generate in team integrations.  Needs to have rights to create alerts.
        :param team_name: The name of the team in OpsGenie that should receive the alert
        :param level: The minimum level a log event must be to be sent to OpsGenie
        """
        super().__init__(level=level)
        conf = opsgenie_sdk.configuration.Configuration()
        conf.api_key["Authorization"] = api_key
        api_client = opsgenie_sdk.api_client.ApiClient(configuration=conf)
        self._alert_api = opsgenie_sdk.AlertApi(api_client=api_client)
        self._team_name = team_name
        self._level_mapping = {
            logging.CRITICAL: "P1",
            logging.ERROR: "P2",
            logging.WARNING: "P3",
            logging.INFO: "P5",
            logging.DEBUG: "P5",
            logging.NOTSET: "P5",
        }

    def emit(self, record: logging.LogRecord):
        """ Send a logging event to OpsGenie """
        if record.levelno < self.level:
            return
        if record.exc_info:
            frame_summary: FrameSummary = extract_tb(record.exc_info[2], 1)[0]
            alias = f"{frame_summary.filename}:{frame_summary.name}:{frame_summary.lineno}"
        else:
            alias = f"{record.pathname}:{record.funcName}:{record.lineno}"
        body = opsgenie_sdk.CreateAlertPayload(
            message=record.getMessage(),
            alias=alias,
            description=self.format(record),
            visible_to=[{"name": self._team_name, "type": "team"}],
            priority=self._level_mapping[record.levelno],
        )
        try:
            self._alert_api.create_alert(create_alert_payload=body)
        except opsgenie_sdk.ApiException as err:
            print(f"Exception when sending log to OpsGenie: {err}\n")
