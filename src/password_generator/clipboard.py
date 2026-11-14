"""Clipboard utilities for password generation"""

import pyperclip



def copy_password(password: str) -> None:
    """Copy a generated password to the system clipboard"""

    if not password:
        raise ValueError("Password cannot be empty")

    try:
        pyperclip.copy(password)
    except pyperclip.PyperclipException as exc:
        raise RuntimeError(
            "Clipboard unavailable. Check your system clipboard support"
        ) from exc
