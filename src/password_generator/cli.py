
"""
Command-line interface for Password Generator.
This module contains the interactive entry point of the application.
"""

from password_generator.generator import generate_password, generate_passwords


def main() -> None:
    print("\n=============================")
    print("   GENERADOR DE CONTRASEÑAS")
    print("=============================\n")

    while True:
        try:
            count = int(input("¿Cuántas contraseñas deseas generar? "))
            length = int(input("¿De cuántos caracteres cada una? "))

            passwords = (
                generate_passwords(count, length)
                if count > 1
                else [generate_password(length)]
            )

            print ("\nContraseñas generadas:\n")
            for index, password in enumerate(passwords, start=1):
                print(f"  {index}. {password}")

        except ValueError as error:
            print(f"\n Error: {error}\nPor favor, introduce números válidos.")
            continue

        again = input("\n¿Deseas generar más contraseñas? (s/n): ").strip().lower()
        if again != "s":
            print("\nGracias por usar el Generador de Contraseñas. ¡Nos vemos! \n")
            break


if __name__ == "__main__":
    main()
