import random

ru_cities = [
	'Астрахань',
	'Абакан',
	'Назрань',
	'Норильск',
	'Красноярск',
	'Курск',
	'Кок'
	]

already_used_city = list()
user_city = None

def get_last_symbol(city):
	if city[-1] in "ьъы":
		return city[-2]
	else:
		return city[-1]

def bot_game():
	last_city = already_used_city[-1]
	get_last_symbol_of_last_city = get_last_symbol(last_city)

	available_cities = list(ac for ac in list(set(ru_cities) - set(already_used_city)) if ac[0] == get_last_symbol_of_last_city.upper())

	if len(available_cities) == 0:
		return ("Ты выиграл")
	else:
		bot_city = random.choice(available_cities)
		# return (bot_city)
		already_used_city.append(bot_city)
		available_cities = list(ac for ac in list(set(ru_cities) - set(already_used_city)) if ac[0] == get_last_symbol_of_last_city.upper())
		if len(available_cities) == 0:
			return ("Я выиграл")
		else:
			return bot_city

def game():
	global user_city
	# user_city = input("Ваш ход: ").strip().capitalize()
	user_city = user_city.strip().capitalize()

	if user_city not in ru_cities:
		return ("Нет такого города")
		# game()
	else:
		if len(already_used_city) == 0:
			already_used_city.append(user_city)
			return bot_game()
		else:
			# if user_city[0] == already_used_city[-1][-1].upper():
			if user_city[0] == get_last_symbol(already_used_city[-1]).upper():
				if user_city in already_used_city:
					return ("Такой город уже был")
					# game()
				else:
					already_used_city.append(user_city)
					return bot_game()
			else:
				return ("Город должен начинаться на {}".format(already_used_city[-1][-1].upper()))
				# game()


# def game_with_user_from_console():
# 	while True:
# 		try:
# 			user_city = input("Ваш ход: ")
# 			game()
# 		except KeyboardInterrupt:
# 			print()
# 			print("Пока!")


# if __name__ == "__main__":
# 	game_with_user_from_console()