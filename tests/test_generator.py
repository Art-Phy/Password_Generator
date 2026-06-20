
from src.password_generator.generator import(
    password_generator,
    multiple_passwords_generator,
)



def test_password_length():
    password = password_generator(12)

    assert len(password) == 12



def test_multiple_passwords_count():
    passwords = multiple_passwords_generator(5, 10)

    assert len(passwords) == 5



def test_invalid_password_length():
    import pytest

    with pytest.raises(ValueError):
        password_generator(0)



def test_invalid_password_count():
    import pytest

    with pytest.raises(ValueError):
        multiple_passwords_generator(0, 10)