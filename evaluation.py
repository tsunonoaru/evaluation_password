password = input("Введите пароль: ")


def is_very_long(password):
	score = 0
	if len(password) > 12:
		score += 2
		return score
	return score


def has_digit(password):
	score = 0
	if any(char.isdigit() for char in password):
		score += 2
		return score
	return score		


def has_upper_letters(password):
	score = 0
	if any(char.isupper() for char in password):
		score += 2
		return score
	return score


def has_lower_letters(password):
	score = 0
	if any(lower.islower() for lower in password):
		score += 2
		return score
	return score		


def has_symbols(password):
	score = 0
	if any(not char.isdigit() and not char.isalpha() for char in password):
	    score += 2
	    return score
	return score    
		

function = [
    is_very_long,
    has_digit,
    has_upper_letters,
    has_lower_letters,
    has_symbols,
]

total_score = 0

for char in function:
	total_score += char(password)

print("Рейтинг пароля:",total_score)	