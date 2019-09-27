import os

import pytest

from opsgenie_logger import OpsGenieHandler


@pytest.mark.skipif(os.environ.get("CI") is not None, reason="Cannot run this test in CI")
class TestIntegration:
    def test_example(self, config):
        import logging

        logger = logging.getLogger()
        handler = OpsGenieHandler(config["api_key"], config["team_name"])
        logger.addHandler(handler)

        logger.error("TEST ERROR")

        try:
            assert True == False
        except:
            logger.exception("There was a problem")


class TestEmit:
    def test_log_level(self, mocker):
        from logging import LogRecord

        handler = OpsGenieHandler("", "")
        handler._alert_api = mocker.MagicMock()

        for log_level, priority in handler._level_mapping.items():
            record = LogRecord("", log_level, "", "", "", [], None)
            handler.emit(record)
            calls = handler._alert_api.create_alert.call_args_list
            assert len(calls) == 1
            kwargs = calls[0][1]
            assert len(kwargs) == 1
            payload = kwargs["create_alert_payload"]
            assert payload.priority == priority
            handler._alert_api.create_alert.reset_mock()

    def test_message(self, mocker):
        from logging import LogRecord

        handler = OpsGenieHandler("", "")
        handler._alert_api = mocker.MagicMock()

        record = LogRecord("", 0, "", "", "test message", [], None)
        handler.emit(record)
        calls = handler._alert_api.create_alert.call_args_list
        kwargs = calls[0][1]
        payload = kwargs["create_alert_payload"]
        assert payload.message == "test message"

    def test_team(self, mocker):
        from logging import LogRecord

        handler = OpsGenieHandler("", "test_team")
        handler._alert_api = mocker.MagicMock()

        record = LogRecord("", 0, "", "", "", [], None)
        handler.emit(record)
        calls = handler._alert_api.create_alert.call_args_list
        kwargs = calls[0][1]
        payload = kwargs["create_alert_payload"]
        assert payload.visible_to == [{"name": "test_team", "type": "team"}]

    def test_alias(self, mocker):
        from logging import LogRecord

        handler = OpsGenieHandler("", "")
        handler._alert_api = mocker.MagicMock()

        record = LogRecord("", 0, "test_path", 123, "", [], None, func="test_func")
        handler.emit(record)
        calls = handler._alert_api.create_alert.call_args_list
        kwargs = calls[0][1]
        payload = kwargs["create_alert_payload"]
        assert payload.alias == "test_path:test_func:123"

    def test_description(self, mocker):
        from logging import LogRecord

        handler = OpsGenieHandler("", "")
        handler._alert_api = mocker.MagicMock()

        record = LogRecord("", 0, "", 0, "", [], None)
        record.exc_text = "bad thing happened"
        handler.emit(record)
        calls = handler._alert_api.create_alert.call_args_list
        kwargs = calls[0][1]
        payload = kwargs["create_alert_payload"]
        assert payload.description == "bad thing happened"

    def test_level(self, mocker):
        from logging import LogRecord

        handler = OpsGenieHandler("", "", 1)
        handler._alert_api = mocker.MagicMock()

        record = LogRecord("", 0, "", 0, "", [], None)
        handler.emit(record)
        calls = handler._alert_api.create_alert.assert_not_called()
