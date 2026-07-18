
"""
Password generation logic
"""

import secrets
import string



def build_character_pool(
        use_lowercase: bool = True,
        use_uppercase: bool = True,
        use_numbers: bool = True,
        use_symbols: bool = True,
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

    if not characters:
        raise ValueError("At least one character set must be enabled.")
    
    return characters



def generate_password(
    length: int,
    use_lowercase: bool = True,
    use_uppercase: bool = True,
    use_numbers: bool = True,
    use_symbols: bool = True,
) -> str:
    """Generate a cryptographically secure password"""

    if length <= 0:
        raise ValueError("Password length must be greater than zero.")
    
    characters = build_character_pool(
        use_lowercase=use_lowercase,
        use_uppercase=use_uppercase,
        use_numbers=use_numbers,
        use_symbols=use_symbols,
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
