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

class CityGame():
	def __init__(self):
		self.already_used_city = list()

	def get_last_symbol(self, city):
		if city[-1] in "ьъы":
			return city[-2]
		else:
			return city[-1]

	def bot_game(self):
		already_used_city = self.already_used_city

		last_city = already_used_city[-1]
		get_last_symbol_of_last_city = self.get_last_symbol(last_city)
		available_cities = list(ac for ac in list(set(ru_cities) - set(already_used_city)) if ac[0] == get_last_symbol_of_last_city.upper())

		if len(available_cities) == 0:
			return ("Ты выиграл")
		else:
			bot_city = random.choice(available_cities)
			already_used_city.append(bot_city)
			available_cities = list(ac for ac in list(set(ru_cities) - set(already_used_city)) if ac[0] == get_last_symbol_of_last_city.upper())
			if len(available_cities) == 0:
				return ("{}. Я выиграл".format(bot_city))
			else:
				return bot_city

	def game(self, user_city):
		try:
			already_used_city = self.already_used_city

			user_city = user_city.strip().capitalize()

			if user_city not in ru_cities:
				return ("Нет такого города")
			else:
				if len(already_used_city) == 0:
					already_used_city.append(user_city)
					return self.bot_game()
				else:
					
					if user_city[0] == self.get_last_symbol(already_used_city[-1]).upper():
						if user_city in already_used_city:
							return ("Такой город уже был")
							
						else:
							already_used_city.append(user_city)
							return self.bot_game()
					else:
						return ("Город должен начинаться на {}".format(already_used_city[-1][-1].upper()))
		except Exception as e:
			print(e)

