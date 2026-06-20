
import pytest


from src.password_generator.generator import generate_password, generate_passwords



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