#!/usr/local/bin/python

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from answers import answers, get_answers

def start(bot, update):
	print("Вызван /start")
	bot.sendMessage(update.message.chat_id, text="Привет! Я бот, который помогает учить Python!")

def talk_to_me(bot, update):
	print('Пришло сообщение: %s' % update.message.text)
	bot.sendMessage(update.message.chat_id, text=get_answers(update.message.text, answers))

def run_bot():
	updater = Updater("295434127:AAE60azMR4b0nashTLGai9DR9GNrjA8UQu0")

	dp = updater.dispatcher
	dp.add_handler(CommandHandler("start", start))
	dp.add_handler(MessageHandler([Filters.text], talk_to_me))

	updater.start_polling()
	updater.idle()

if __name__ == "__main__":
	run_bot()