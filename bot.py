#!/usr/local/bin/python

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from answers import answers, get_answers
from cities import game as m_game
import cities
import datetime
from countwords import countwords
from calc import calc as m_calc
from wordscalc import wordscalc as m_wordscalc
game_flag = False

def start(bot, update):
	print("Вызван /start")
	bot.sendMessage(update.message.chat_id, text="Привет! Я бот, который помогает учить Python!")

def talk_to_me(bot, update):
	global game_flag
	if not game_flag:
		print('Пришло сообщение: %s' % update.message.text)
		bot.sendMessage(update.message.chat_id, text=get_answers(update.message.text, answers))
	else:
		cities.user_city = update.message.text
		bot.sendMessage(update.message.chat_id, text=m_game())


def time(bot, update):
	bot.sendMessage(update.message.chat_id, text=datetime.datetime.now().strftime("%A, %d.%m.%y, %H:%M:%S"))

def game(bot, update):
	global game_flag
	game_flag = True
	print("Вызван /game")
	bot.sendMessage(update.message.chat_id, text="Поиграем в города. Начинай.")

def stopgame(bot, update):
	global game_flag
	game_flag = False
	print("Вызван /stopgame")
	bot.sendMessage(update.message.chat_id, text="Стоп игра.")
	cities.already_used_city = list()

def count(bot, update):
	count = str(countwords(update.message.text))
	if count[-1] == "1":
		suffix = "о"
	elif count[-1] in ("234"):
		suffix = "a"
	else:
		suffix = ""
	answer = "В этой фразе {} слов{}.".format(count, suffix)
	bot.sendMessage(update.message.chat_id, text=answer)

def calc(bot, update):
	expr = update.message.text
	expr = expr.replace("/calc", "")
	print(expr)
	bot.sendMessage(update.message.chat_id, text=m_calc(expr))

def wordscalc(bot, update):
	expr = update.message.text
	expr = expr.replace("/wordscalc", "")
	print(expr)
	bot.sendMessage(update.message.chat_id, text=m_wordscalc(expr))


def run_bot():
	updater = Updater("295434127:AAE60azMR4b0nashTLGai9DR9GNrjA8UQu0")

	dp = updater.dispatcher
	dp.add_handler(CommandHandler("start", start))
	dp.add_handler(CommandHandler("time", time))
	dp.add_handler(CommandHandler("game", game))
	dp.add_handler(CommandHandler("stopgame", stopgame))
	dp.add_handler(CommandHandler("count", count))
	dp.add_handler(CommandHandler("calc", calc))
	dp.add_handler(CommandHandler("wordscalc", wordscalc))
	dp.add_handler(MessageHandler([Filters.text], talk_to_me))

	updater.start_polling()
	updater.idle()

if __name__ == "__main__":
	run_bot()