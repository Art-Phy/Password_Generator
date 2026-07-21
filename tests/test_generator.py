
import pytest


from src.password_generator.generator import generate_password, generate_passwords
from password_generator.generator import AMBIGUOUS_CHARACTERS, generate_password


def test_password_length():
    password = generate_password(12)

    assert len(password) == 12



def test_multiple_passwords_count():
    passwords = generate_passwords(5, 10)

    assert len(passwords) == 5



def test_invalid_password_length():
    with pytest.raises(ValueError):
        generate_password(0)



def test_invalid_password_count():
    with pytest.raises(ValueError):
        generate_passwords(0, 10)



def test_generate_safe_password_excludes_ambiguous_characters():
    password = generate_password(
        length=500,
        exclude_ambiguous=True,
    )

    assert len(password) == 500

    assert not any(
        character in AMBIGUOUS_CHARACTERS
        for character in password
    )
