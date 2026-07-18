
"""
Command-line interface for Password Generator.
This module contains the interactive entry point of the application.
"""

import argparse

from dataclasses import asdict
from password_generator.generator import generate_password, generate_passwords
from password_generator.profiles import PROFILES, get_profile


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

    parser.add_argument(
        "-p",
        "--profile",
        choices=PROFILES.keys(),
        help="Use a predefined password generation profile.",
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



def run_cli_mode(
    count: int,
    config: dict[str, int | bool],
) -> None:
    passwords = (
        generate_passwords(
            count=count,
            **config,
        )
        if count > 1
        else [
            generate_password(
                **config,
            )
        ]
    )

    for password in passwords:
        print(password)



def resolve_generation_config(args: argparse.Namespace) -> dict[str, int | bool]:
    """Resolve password generation settings from CLI arguments"""

    if args.profile:
        config = asdict(get_profile(args.profile))
    else:
        config = {
            "length": args.length or 12,
            "use_lowercase": True,
            "use_uppercase": True,
            "use_numbers": True,
            "use_symbols": True,
        }
    
    if args.length is not None:
        config["length"] = args.length

    return config



def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    if args.length is None and args.profile is None:
        run_interactive_mode()
        return
    
    try:
        config = resolve_generation_config(args)

        run_cli_mode(
            count=args.count,
            config=config,
            )
    except ValueError as error:
        parser.error(str(error))


if __name__ == "__main__":
    main()
