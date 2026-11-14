"""Tests for CLI clipboard integration."""

from unittest.mock import patch

import pytest

from password_generator.cli import run_cli_mode


CONFIG = {
    "length": 16,
    "use_lowercase": True,
    "use_uppercase": True,
    "use_numbers": True,
    "use_symbols": True,
    "exclude_ambiguous": False,
}



def test_copy_does_not_display_password(capsys):
    """Copied passwords must not appear in CLI output."""

    with (
        patch(
            "password_generator.cli.generate_password",
            return_value="TestSecret123!",
        ),
        patch(
            "password_generator.cli.copy_password",
        ) as mock_copy,
    ):
        run_cli_mode(
            count=1,
            config=CONFIG,
            copy=True,
        )

    output = capsys.readouterr().out

    mock_copy.assert_called_once_with("TestSecret123!")

    assert "TestSecret123!" not in output
    assert "Password copied to clipboard" in output



def test_copy_rejects_multiple_passwords():
    """Clipboard mode must reject multiple passwords"""

    with pytest.raises(
        ValueError,
        match="--copy only supports generating one password",
    ):
        run_cli_mode(
            count=5,
            config=CONFIG,
            copy=True,
        )
