
"""
Password generation utilities.
"""

import secrets
import string



def password_generator(longitud: int) -> str:
    if longitud <= 0:
        raise ValueError("La longitud debe ser un número positivo mayor que 0.")
    
    caracteres = string.ascii_letters + string.digits + string.punctuation

    return "".join(secrets.choice(caracteres) for _ in range(longitud))



def multiple_passwords_generator(cantidad: int, longitud: int) -> list[str]:
    if cantidad <= 0:
        raise ValueError("La cantidad debe ser mayor que 0.")
    
    return [password_generator(longitud) for _ in range(cantidad)]
