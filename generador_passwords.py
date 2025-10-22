### Generador de Contraseñas Aleatorias ###

# se importan los módulos necesarios para crear el código
import random
import string

def password_generator(longitud=''):

    # definimos los caracteres que se pueden usar
    caracteres = string.ascii_letters + string.digits + string.punctuation

    # decimos que se genere una contraseña
    password = ''.join(random.choice(caracteres) for _ in range(longitud))
    return password

# creamos una función para las múltiples contraseñas
def multiple_passwords_generator(cantidad, longitud=''):
    passwords = []
    for _ in range(cantidad):
        passwords.append(password_generator(longitud))
    return passwords

# hacemos que el usuario decida la cantidad y la longitud de la/s contraseña/s
passwords_quantity = int(input("¿Cuántas contraseñas necesitas? "))
password_length = int(input("¿Cuántos caracteres quieres que tenga? "))

# generamos las contraseñas
passwords = multiple_passwords_generator(passwords_quantity, password_length)

# mostrar las contraseñas generadas
for p, password in enumerate(passwords, 1):
    print(f"Contraseña {p}: {password}")
