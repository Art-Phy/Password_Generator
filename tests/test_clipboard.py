"""Tests for clipboard utilities."""

from unittest.mock import patch

import pyperclip
import pytest

from password_generator.clipboard import copy_password



def test_copy_password():
    """Password should be sent to the clipboard."""

    with patch(
        "password_generator.clipboard.pyperclip.copy"
    ) as mock_copy:
        copy_password("Test123!")

    mock_copy.assert_called_once_with("Test123!")



def test_copy_password_rejects_empty_password():
    """Empty passwords should be rejected."""

    with pytest.raises(ValueError):
        copy_password("")



def test_copy_password_handles_unavailable_clipboard():
    """Clipboard errors should be handled."""

    with patch(
        "password_generator.clipboard.pyperclip.copy",
        side_effect=pyperclip.PyperclipException(),
    ):
        with pytest.raises(RuntimeError, match="Clipboard unavailable"):
            copy_password("Test123!")
