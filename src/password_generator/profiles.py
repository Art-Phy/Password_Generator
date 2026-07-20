
"""Predefine password generation profiles"""

from dataclasses import dataclass



@dataclass(frozen=True)
class PasswordProfile:
    """Configuration for a predefined password generation profile"""

    length: int
    charset: str



PROFILES = {
    "web": PasswordProfile(
        length=16,
        charset="all",
    ),

    "wifi": PasswordProfile(
        length=24,
        charset="safe",
    ),

    "pin": PasswordProfile(
        length=6,
        charset="numbers",
    ),

    "secure": PasswordProfile(
        length=32,
        charset="all",
    ),
}



def get_profile(name: str) -> PasswordProfile:
    """Return a predefined password generation profile"""

    try:
        return PROFILES[name]
    except KeyError as exc:
        raise ValueError(f"Unkown profile: {name}") from exc
