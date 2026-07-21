
"""Predefined character sets"""

from dataclasses import dataclass



@dataclass(frozen=True)
class CharacterSet:
    """Character set configuration"""
    
    use_lowercase: bool = True
    use_uppercase: bool = True
    use_numbers: bool = True
    use_symbols: bool = True
    exclude_ambiguous: bool = False


CHARSETS: dict[str, CharacterSet] = {
    "all": CharacterSet(),

    "letters": CharacterSet(
        use_numbers=False,
        use_symbols=False,
    ),

    "lowercase": CharacterSet(
        use_uppercase=False,
        use_numbers=False,
        use_symbols=False,
    ),

    "uppercase": CharacterSet(
        use_lowercase=False,
        use_numbers=False,
        use_symbols=False,
    ),

    "numbers": CharacterSet(
        use_lowercase=False,
        use_uppercase=False,
        use_symbols=False,
    ),

    "alphanumeric": CharacterSet(
        use_symbols=False,
    ),

    "safe": CharacterSet(
        exclude_ambiguous=True,
    ),
}



def get_charset(name: str) -> CharacterSet:
    """Return a predefined character set"""

    try:
        return CHARSETS[name]
    except KeyError as exc:
        raise ValueError(f"Unknown character set: {name}") from exc
