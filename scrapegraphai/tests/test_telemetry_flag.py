"""Tests for the telemetry opt-out flag.

These cover the environment variable path, which previously read its value from
the config file instead of from the variable, so `SCRAPEGRAPHAI_TELEMETRY_ENABLED=false`
left telemetry enabled.
"""

import configparser

import pytest

from scrapegraphai.telemetry.telemetry import (
    _check_config_and_environ_for_telemetry_flag,
    _parse_bool,
)


def _config(**defaults):
    cfg = configparser.ConfigParser()
    cfg["DEFAULT"] = {k: str(v) for k, v in defaults.items()}
    return cfg


class TestParseBool:
    @pytest.mark.parametrize("value", ["false", "False", "FALSE", "no", "off", "0", "  false  "])
    def test_falsey_spellings(self, value):
        assert _parse_bool(value) is False

    @pytest.mark.parametrize("value", ["true", "True", "yes", "on", "1"])
    def test_truthy_spellings(self, value):
        assert _parse_bool(value) is True

    def test_rejects_nonsense(self):
        with pytest.raises(ValueError):
            _parse_bool("maybe")


class TestTelemetryFlag:
    def test_defaults_to_the_given_default(self):
        assert _check_config_and_environ_for_telemetry_flag(True, _config()) is True

    def test_config_file_can_disable(self):
        cfg = _config(telemetry_enabled="False")
        assert _check_config_and_environ_for_telemetry_flag(True, cfg) is False

    def test_env_var_disables_with_no_config_key(self, monkeypatch):
        """The regression. Previously returned True, because the value was read
        out of the config file rather than out of the environment variable."""
        monkeypatch.setenv("SCRAPEGRAPHAI_TELEMETRY_ENABLED", "false")
        assert _check_config_and_environ_for_telemetry_flag(True, _config()) is False

    def test_env_var_overrides_the_config_file(self, monkeypatch):
        monkeypatch.setenv("SCRAPEGRAPHAI_TELEMETRY_ENABLED", "false")
        cfg = _config(telemetry_enabled="True")
        assert _check_config_and_environ_for_telemetry_flag(True, cfg) is False

    def test_env_var_can_also_enable(self, monkeypatch):
        monkeypatch.setenv("SCRAPEGRAPHAI_TELEMETRY_ENABLED", "true")
        cfg = _config(telemetry_enabled="False")
        assert _check_config_and_environ_for_telemetry_flag(True, cfg) is True

    def test_unparseable_env_var_leaves_the_flag_alone(self, monkeypatch):
        monkeypatch.setenv("SCRAPEGRAPHAI_TELEMETRY_ENABLED", "banana")
        cfg = _config(telemetry_enabled="False")
        assert _check_config_and_environ_for_telemetry_flag(True, cfg) is False

    def test_unset_env_var_leaves_the_config_in_charge(self, monkeypatch):
        monkeypatch.delenv("SCRAPEGRAPHAI_TELEMETRY_ENABLED", raising=False)
        cfg = _config(telemetry_enabled="False")
        assert _check_config_and_environ_for_telemetry_flag(True, cfg) is False
