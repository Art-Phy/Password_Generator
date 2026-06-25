
"""
Command-line interface for Password Generator.
This module contains the interactive entry point of the application.
"""

import argparse

from password_generator.generator import generate_password, generate_passwords

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="password-generator",
        description="Generate secure random passwords from the command line.",
    )

    parser.add_argument(
        "-l",
        "--length",
        type=int,
        default=None,
        help="Password length.",
    )

    parser.add_argument(
        "-c",
        "--count",
        type=int,
        default=1,
        help="Number of passwords to generate.",
    )

    return parser



def run_interactive_mode() -> None:
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



def run_cli_mode(length: int, count: int) -> None:
    passwords = (
        generate_passwords(count, length)
        if count > 1
        else [generate_password(length)]
    )

    for password in passwords:
        print(password)



def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    if args.length is None:
        run_interactive_mode()
        return
    
    try:
        run_cli_mode(args.length, args.count)
    except ValueError as error:
        parser.error(str(error))


if __name__ == "__main__":
    main()
