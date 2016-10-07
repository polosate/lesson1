#!/usr/local/bin/python

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from answers import answers, get_answers
from cities import CityGame
import cities
import datetime
from countwords import countwords
from calc import calc as m_calc
from wordscalc import wordscalc as m_wordscalc

class Bot():

	def __init__(self):
		self.user_games = dict()


	def start(self, bot, update):
		print("Вызван /start")
		bot.sendMessage(update.message.chat_id, text="Привет! Я бот, который помогает учить Python!")


	def talk_to_me(self, bot, update):
		user_games = self.user_games
		if not user_games.get(update.message.chat_id):
			print('Пришло сообщение: %s' % update.message.text)
			bot.sendMessage(update.message.chat_id, text=get_answers(update.message.text, answers))
		else:
			user_city = user_games.get(update.message.chat_id).game(update.message.text)
			bot.sendMessage(update.message.chat_id, text=user_city)


	def time(self, bot, update):
		bot.sendMessage(update.message.chat_id, text=datetime.datetime.now().strftime("%A, %d.%m.%y, %H:%M:%S"))


	def game(self, bot, update):
		user_games = self.user_games

		user_games[update.message.chat_id] = CityGame()
		print("Вызван /game")
		bot.sendMessage(update.message.chat_id, text="Поиграем в города. Начинай.")


	def stopgame(self, bot, update):
		user_games = self.user_games
		print("Вызван /stopgame")
		del user_games[update.message.chat_id]
		bot.sendMessage(update.message.chat_id, text="Стоп игра.")
		

	def count(self, bot, update):
		count = str(countwords(update.message.text))
		if count[-1] == "1":
			suffix = "о"
		elif count[-1] in ("234"):
			suffix = "a"
		else:
			suffix = ""
		answer = "В этой фразе {} слов{}.".format(count, suffix)
		bot.sendMessage(update.message.chat_id, text=answer)


	def calc(self, bot, update):
		expr = update.message.text
		expr = expr.replace("/calc", "")
		print(expr)
		bot.sendMessage(update.message.chat_id, text=m_calc(expr))


	def wordscalc(self, bot, update):
		print(update.message.text.replace("/wordscalc", ""))
		bot.sendMessage(update.message.chat_id, text=m_wordscalc(update.message.text.replace("/wordscalc", "")))


def run_bot():

	bot = Bot()

	updater = Updater("295434127:AAE60azMR4b0nashTLGai9DR9GNrjA8UQu0")

	dp = updater.dispatcher
	dp.add_handler(CommandHandler("start", bot.start))
	dp.add_handler(CommandHandler("time", bot.time))
	dp.add_handler(CommandHandler("game", bot.game))
	dp.add_handler(CommandHandler("stopgame", bot.stopgame))
	dp.add_handler(CommandHandler("count", bot.count))
	dp.add_handler(CommandHandler("calc", bot.calc))
	dp.add_handler(CommandHandler("wordscalc", bot.wordscalc))
	dp.add_handler(MessageHandler([Filters.text], bot.talk_to_me))

	updater.start_polling()
	updater.idle()

if __name__ == "__main__":
	run_bot()