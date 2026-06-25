
"""
Password generation utilities.
"""

import secrets
import string



def generate_password(length: int) -> str:
    if length <= 0:
        raise ValueError("La longitud debe ser un número positivo mayor que 0.")
    
    characters = string.ascii_letters + string.digits + string.punctuation

    return "".join(secrets.choice(characters) for _ in range(length))



def generate_passwords(count: int, length: int) -> list[str]:
    if count <= 0:
        raise ValueError("La cantidad debe ser mayor que 0.")
    
    return [generate_password(length) for _ in range(count)]
