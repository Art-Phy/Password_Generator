
"""Predefine password generation profiles"""

from dataclasses import dataclass



@dataclass(frozen=True)
class PasswordProfile:
    """Configuration for a predefined password generation profile"""

    length: int
    use_lowercase: bool = True
    use_uppercase: bool = True
    use_numbers: bool = True
    use_symbols: bool = True



PROFILES: dict[str, PasswordProfile] = {
    "web": PasswordProfile(
        length=16,
    ),
    "wifi": PasswordProfile(
        length=24,
        use_symbols=False,
    ),
    "pin": PasswordProfile(
        length=6,
        use_lowercase=False,
        use_uppercase=False,
        use_numbers=True,
        use_symbols=False,
    ),
    "secure": PasswordProfile(
        length=32,
    ),
}



def get_profile(name: str) -> PasswordProfile:
    """Return a predefined password generation profile"""

    try:
        return PROFILES[name]
    except KeyError as exc:
        raise ValueError(f"Unkown profile: {name}") from exc
