
"""
Command-line interface for Password Generator.
This module contains the interactive entry point of the application.
"""

from src.password_generator.generator import(
    multiple_passwords_generator,
    password_generator,
)


def main() -> None:
    print("\n=============================")
    print("   GENERADOR DE CONTRASEÑAS")
    print("=============================\n")

    while True:
        try:
            cantidad = int(input("¿Cuántas contraseñas deseas generar? "))
            longitud = int(input("¿De cuántos caracteres cada una? "))

            passwords = (
                multiple_passwords_generator(cantidad, longitud)
                if cantidad < 1
                else [password_generator(longitud)]
            )

            print ("\nContraseñas generadas:\n")
            for i, password in enumerate(passwords, start=1):
                print(f"  {i}. {password}")

        except ValueError as error:
            print(f"\n Error: {error}\nPor favor, introduce números válidos.")
            continue

        again = input("\n¿Deseas generar más contraseñas? (s/n): ").strip().lower()
        if again != "s":
            print("\nGracias por usar el Generador de Contraseñas. ¡Nos vemos! \n")
            break


if __name__ == "__main__":
    main()
