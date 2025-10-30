"""
=============================
   MÓDULO DE UTILIDADES
=============================

Autor: Art-Phy
Descripción:
  Este módulo contiene funciones reutilizables para generar contraseñas
  aleatorias seguras. Se puede importar fácilmente desde otros programas.

Incluye:
- Generación de una contraseña individual.
- Generación de múltiples contraseñas.
"""

import random
import string


def password_generator(longitud: int) -> str:
    if longitud <= 0:
        raise ValueError("La longitud debe ser un número positivo mayor que 0.")

    # Definimos los caracteres válidos: letras, dígitos y símbolos
    caracteres = string.ascii_letters + string.digits + string.punctuation

    # Generamos la contraseña uniendo caracteres aleatorios
    password = ''.join(random.choice(caracteres) for _ in range(longitud))
    return password


def multiple_passwords_generator(cantidad: int, longitud: int) -> list:
    if cantidad <= 0:
        raise ValueError("La cantidad debe ser mayor que 0.")

    return [password_generator(longitud) for _ in range(cantidad)]
