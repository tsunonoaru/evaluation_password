def is_very_long(password):
    return (len(password) > 12) * 2


def has_digit(password):
    return 2 if any(char.isdigit() for char in password) else 0


def has_upper_letters(password):
    return 2 if any(char.isupper() for char in password) else 0


def has_lower_letters(password):
    return 2 if any(char.islower() for char in password) else 0


def has_symbols(password):
    return 2 if any(not char.isdigit() and not char.isalpha() for char in password) else 0


if __name__ == "__main__":
    password = input("Введите пароль: ")

    functions = [
        is_very_long,
        has_digit,
        has_upper_letters,
        has_lower_letters,
        has_symbols,
    ]

    score = 0

    for func in functions:
        score += func(password)

    print("Рейтинг пароля:", score)
