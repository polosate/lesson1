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

# Функция добавляет горрод в список уже названных, или запрашивает другой
# def append_or_reset_city(city, index_of_last_symbol):
# 	last_city = already_used_city[-1]
# 	# Проверка, что город начинается на правильную букву,
# 	if last_city[index_of_last_symbol] == city[0].lower():
# 		# Проверка, если город уже был, просим другой
# 		if city in already_used_city:
# 			print("{} уже был. Давай другой на букву {}".format(city, get_last_symbol_of_last_city().upper()))
# 			game()
# 		# Если буква правильная и такого города ещё не было, принимает город
# 		print("{}! Принято!_1".format(city))
# 		already_used_city.append(city)
# 		bot_game(get_last_symbol_of_last_city())
# 	else:
# 		print("Город должен начинаться на {}!".format(last_city[index_of_last_symbol].upper()))		
# 		game()

# # Функция возвращает последнюю букву последненего города, на которую может начинаться другой город
# def get_last_symbol_of_last_city():
# 	if already_used_city[-1][-1] in 'ьъы':
# 		return already_used_city[-1][-2]
# 	else:
# 		return already_used_city[-1][-1]

# #  Функция возвращает список доступных для выбора городов, как разницу между тем что есть вообще, и тем, что уже называли игроки
# def get_availables_cities(char):
# 	return list(ac for ac in list(set(ru_cities) - set(already_used_city)) if ac[0] == char.upper())

# def bot_game(char):	
# 	availbale_cities_for_bot = get_availables_cities(char)
# 	try:
# 		bot_city = random.choice(availbale_cities_for_bot)
# 		print("Мой ход: {}".format(bot_city))
# 		already_used_city.append(bot_city)
# 		if len(get_availables_cities(get_last_symbol_of_last_city())) == 0:
# 			print(("Я выиграл! Городов на {} больше не осталось!").format(get_last_symbol_of_last_city().capitalize()))
# 		else:
# 			game()			
# 	except IndexError:
# 		print(("Ты выиграл! Городов на {} больше не осталось-(((").format(get_last_symbol_of_last_city().capitalize()))	

# def game():
# 	city = input("Ваш ход: ").strip().capitalize()

# 	# Проверка, есть ли такой город вообще. Если нет, начать игру сначала
# 	if city not in ru_cities:
# 		print ("Нет такого города в России!")
# 		game()

# 	try:
# 		last_city = already_used_city[-1]
# 		if last_city[-1] not in 'ьъы':
# 			append_or_reset_city(city, -1)
# 		else:
# 			append_or_reset_city(city, -2)
# 	except IndexError:
# 		# Если городов в списке названных нет, добавляем туда город
# 		print(("{}! Принято!").format(city))
# 		already_used_city.append(city)	
# 		bot_game(get_last_symbol_of_last_city())

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