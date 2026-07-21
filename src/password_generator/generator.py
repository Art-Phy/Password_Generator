
"""
Password generation logic
"""

import secrets
import string


AMBIGUOUS_CHARACTERS = frozenset("O0Il1|/\\'\"`")


def build_character_pool(
        use_lowercase: bool,
        use_uppercase: bool,
        use_numbers: bool,
        use_symbols: bool,
        exclude_ambiguous: bool = False,
) -> str:
    """Build the character pool used to generate passwords"""

    characters = ""

    if use_lowercase:
        characters += string.ascii_lowercase

    if use_uppercase:
        characters += string.ascii_uppercase

    if use_numbers:
        characters += string.digits

    if use_symbols:
        characters += string.punctuation
    
    if exclude_ambiguous:
        characters = "".join(
            character
            for character in characters
            if character not in AMBIGUOUS_CHARACTERS
        )

    if not characters:
        raise ValueError("At least one character set must be enabled.")
    
    return characters



def generate_password(
    length: int,
    use_lowercase: bool = True,
    use_uppercase: bool = True,
    use_numbers: bool = True,
    use_symbols: bool = True,
    exclude_ambiguous: bool = False,
) -> str:
    """Generate a cryptographically secure password"""

    if length <= 0:
        raise ValueError("Password length must be greater than zero.")
    
    characters = build_character_pool(
        use_lowercase=use_lowercase,
        use_uppercase=use_uppercase,
        use_numbers=use_numbers,
        use_symbols=use_symbols,
        exclude_ambiguous=exclude_ambiguous,
    )

    return "".join(secrets.choice(characters) for _ in range(length))




def generate_passwords(
        count: int,
        length: int,
        use_lowercase: bool = True,
        use_uppercase: bool = True,
        use_numbers: bool = True,
        use_symbols: bool = True,
) -> list[str]:
    """Generate multiple cryptographycally secure passwords"""

    if count <= 0:
        raise ValueError("Password count must be greater than zero.")
    
    return [
        generate_password(
            length=length,
            use_lowercase=use_lowercase,
            use_uppercase=use_uppercase,
            use_numbers=use_numbers,
            use_symbols=use_symbols,
        )
        for _ in range(count)
    ]
