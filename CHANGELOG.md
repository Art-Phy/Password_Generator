## CHANGELOG

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to Semantic Versioning.

---

### [1.5.0] - 2026-11-14

#### Added

- Added clipboard support through the new `--copy` CLI option.
- Added the `clipboard.py` module for system clipboard integration using `pyperclip`.
- Added support for combining `--copy` with password profiles, character sets, and custom lengths.
- Added support for displaying password entropy and strength alongside clipboard operations using `--show-strength`.
- Added dedicated tests for clipboard functionality and CLI integration.
- Added error handling for unavailable or unsupported system clipboards.

#### Changed

- Updated the CLI to copy generated passwords without displaying their contents in the terminal when using `--copy`.
- Restricted clipboard operations to a single password per execution.
- Improved CLI argument validation to reject incompatible combinations of `--copy` and multiple passwords.
- Extended CLI error handling to provide clear messages when clipboard operations fail.
- Added `pyperclip` as a project dependency.
- Preserved the existing password generation behavior when clipboard support is not requested.

---

### [1.4.0] - 2026-09-11

#### Added

- Added password entropy estimation based on password length and character pool size.
- Added password strength classification with four levels:
    - `Weak`
    - `Medium`
    - `Strong`
    - `Very Strong`
- Added the `--show-strength` CLI option to display estimated entropy and password strength.
- Added dedicated tests for entropy calculation and strength classification.
- Added boundary tests for strength rating thresholds

#### Changed

- Extended the CLI to calculate password strength using the actual character set selected for generation.
- Password strength estimation now respects profiles, custom characater sets, safe mode, and custom password lengths.
- Kept strength analysis optional to preserve clean default CLI output.

---

### [1.3.0] - 2026-07-21

#### Added

- Added predefined password generation profiles:
    * web
    * wifi
    * pin
    * secure
- Added configurable character sets through the new --charset option:
    * all
    * letters
    * lowercase
    * uppercase
    * numbers
    * alphanumeric
    * safe
- Added support for overriding profile defaults with --length and --charset.
- Added safe password generation by excluding visually ambiguous characters.
- Added dedicated tests for safe password generation.

#### Changed

- Refactored password generation to support configurable character types.
- Simplified password profiles by associating each profile with a predefined character set.
- Improved configuration resolution between default values, profiles and explicit CLI arguments.
- Separated password profiles and character-set definitions into dedicated modules.

---

### [1.2.0] - 2026-06-25

#### Added

- Complete project restructuring following the `src/` layout.
- Added packaging support using `pyproject.toml`.
- Added installable `password-generator` command.
- Added CLI argument support using `argparse`.
- Added both interactive and non-interactive execution modes.
- Added automated tests with `pytest`.
- Added `pytest` configuration to `pyproject.toml`.

#### Changed

- Replaced the `random` module with `secrets` for cryptographically secure password generation.
- Renamed the main functions to `generate_password()` and `generate_passwords()`.
- Refactored the project structure to separate user interface from business logic.
- Improved internal code organization and readability.
- Updated the project documentation.

#### Fixed

- Fixed multiple password generation in interactive mode.
- Improved input parameter validation.
- Removed temporary files and unnecessary repository artifacts.
- Updated `.gitignore` to properly exclude development-generated files.

---

### [1.1.0] - 2025-10-29

#### Main Improvements

- Refactored the project into separate modules (`main.py` and `utils.py`).
- Added input validation and exception handling.
- Added program flow control to allow generating multiple passwords without restarting.
- Prepared the project for future unit testing and CLI improvements.

#### Technical Changes

- `password_generator()` now raises `ValueError` for invalid password lengths.
- Added `multiple_passwords_generator()` with input validation.
- Added docstrings to all functions.
- Adopted the `if __name__ == "__main__":` execution pattern in `main.py`.

#### Other

- Added `requirements.txt` (no external dependencies).
- Improved code comments and overall project structure.
- Prepared the project for the `v1.1.0` release and GitHub versioning workflow.
