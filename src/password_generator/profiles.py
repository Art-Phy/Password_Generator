
"""Predefine password generation profiles"""

from dataclasses import dataclass



@dataclass(frozen=True)
class PasswordProfile:
    """Configuration for a predefined password generation profile"""

    length: int
    use_lowecase: bool = True
    use_uppercase: bool = True
    use_numbers: bool = True
    use_symbols: bool = True
