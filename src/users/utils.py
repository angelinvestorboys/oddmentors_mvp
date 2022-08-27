from string import (
                    # punctuation,
                    # whitespace,
                    digits,
                    ascii_lowercase,
                    ascii_uppercase)
from django.contrib.auth.hashers import check_password


def password_verification_logic(
        old_password,
        new_password,
        verify_password,
        user):

    old_password = old_password.strip()
    new_password = new_password.strip()
    verify_password = verify_password.strip()

    MIN_SIZE = 6
    MAX_SIZE = 20
    password_size = len(new_password)

    if not user.check_password(old_password):
        return (False, "Incorrect password")

    if new_password != verify_password:
        return (False, "Passwords do not match")

    if password_size < MIN_SIZE or password_size > MAX_SIZE:
        return (False, "Inputed password does must have \
            a minimum of 6 and maximum of 20 characters")

    # valid_chars = {'-', '_', '.', '!', '@', '#', '$', '^', '&', '(', ')'}
    # invalid_chars = set(punctuation + whitespace) - valid_chars

    # for char in invalid_chars:
    #     if char in new_password:
    #         return False

    password_has_digit = False
    for char in new_password:
        if char in digits:
            password_has_digit = True
            break

    if not password_has_digit:
        return (False, "Inputed password needs to contain a lowercase, Uppercase and digit"
)
    password_has_lowercase = False

    for char in new_password:
        if char in ascii_lowercase:
            password_has_lowercase = True
            break

    if not password_has_lowercase:
        return (False, "Inputed password needs to contain a lowercase, Uppercase and digit")

    password_has_uppercase = False

    for char in new_password:
        if char in ascii_uppercase:
            password_has_uppercase = True
            break

    if not password_has_uppercase:
        return (False, "Inputed password needs to contain a lowercase, Uppercase and digit")

    return (True, "password successfully changed")
