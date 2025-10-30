"""
=============================
 GENERADOR DE CONTRASEÑAS (v2)
=============================

Autor: Art-Phy
Descripción:
  Programa interactivo que permite generar una o varias contraseñas
  aleatorias seguras según los parámetros elegidos por el usuario.

Mejoras respecto a la versión anterior:
- Estructura modular (main + utils).
- Validación de entradas del usuario.
- Manejo de excepciones.
- Preparado para futuras pruebas unitarias.
"""

from utils import password_generator, multiple_passwords_generator


def main():
    print("\n=============================")
    print("  🔐 GENERADOR DE CONTRASEÑAS")
    print("=============================\n")

    while True:
        try:
            cantidad = int(input("¿Cuántas contraseñas deseas generar? "))
            longitud = int(input("¿De cuántos caracteres cada una? "))

            passwords = (
                multiple_passwords_generator(cantidad, longitud)
                if cantidad > 1
                else [password_generator(longitud)]
            )

            print("\nContraseñas generadas:\n")
            for i, p in enumerate(passwords, start=1):
                print(f"  {i}. {p}")

        except ValueError as e:
            print(f"\n❌ Error: {e}\nPor favor, introduce números válidos.")
            continue

        # Preguntar si el usuario desea generar más contraseñas
        again = input("\n¿Deseas generar más contraseñas? (s/n): ").strip().lower()
        if again != 's':
            print("\nGracias por usar el Generador de Contraseñas. ¡Hasta luego! 👋\n")
            break


if __name__ == "__main__":
    main()
