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

        # noinspection PyBroadException
        try:
            assert True == False  # noQA
        except:
            logger.exception("There was a problem")


class TestEmit:
    def test_log_level(self, mocker):
        from logging import LogRecord

        requests = mocker.patch("opsgenie_logger.requests")
        handler = OpsGenieHandler("", "")

        for log_level, priority in handler._level_mapping.items():
            record = LogRecord("", log_level, "", "", "", [], None)
            handler.emit(record)
            calls = requests.post.call_args_list
            assert len(calls) == 1
            kwargs = calls[0][1]
            assert len(kwargs) == 2
            payload = kwargs["json"]
            assert payload["priority"] == priority
            requests.post.reset_mock()

    def test_message(self, mocker):
        from logging import LogRecord

        requests = mocker.patch("opsgenie_logger.requests")
        handler = OpsGenieHandler("", "")

        record = LogRecord("", 0, "", "", "test message", [], None)
        handler.emit(record)
        calls = requests.post.call_args_list
        kwargs = calls[0][1]
        payload = kwargs["json"]
        assert payload["message"] == "test message"

    def test_team(self, mocker):
        from logging import LogRecord

        requests = mocker.patch("opsgenie_logger.requests")
        handler = OpsGenieHandler("", "test_team")

        record = LogRecord("", 0, "", "", "", [], None)
        handler.emit(record)
        calls = requests.post.call_args_list
        kwargs = calls[0][1]
        payload = kwargs["json"]
        assert payload["visible_to"] == [{"name": "test_team", "type": "team"}]

    def test_alias(self, mocker):
        from logging import LogRecord

        requests = mocker.patch("opsgenie_logger.requests")
        handler = OpsGenieHandler("", "")

        record = LogRecord("", 0, "test_path", 123, "", [], None, func="test_func")
        handler.emit(record)
        calls = requests.post.call_args_list
        kwargs = calls[0][1]
        payload = kwargs["json"]
        assert payload["alias"] == "test_path:test_func:123"

    def test_description(self, mocker):
        from logging import LogRecord

        requests = mocker.patch("opsgenie_logger.requests")
        handler = OpsGenieHandler("", "")

        record = LogRecord("", 0, "", 0, "", [], None)
        record.exc_text = "bad thing happened"
        handler.emit(record)
        calls = requests.post.call_args_list
        kwargs = calls[0][1]
        payload = kwargs["json"]
        assert payload["description"] == "\nbad thing happened"

    def test_level(self, mocker):
        from logging import LogRecord, ERROR

        requests = mocker.patch("opsgenie_logger.requests")
        handler = OpsGenieHandler("", "", 1)

        record = LogRecord("", 0, "", 0, "", [], None)
        handler.emit(record)
        requests.post.assert_not_called()

        handler = OpsGenieHandler("", "", "WARNING")
        record = LogRecord("", ERROR, "", 0, "", [], None)
        handler.emit(record)
        requests.post.assert_called_once()
