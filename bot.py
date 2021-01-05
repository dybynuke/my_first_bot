# -*- coding: utf8 -*-

import telebot
import os
from telebot import types

a = "[12:00 - 13:50] Комплексное обеспечение безопасности инормационных систем(л)\nhttps://us04web.zoom.us/j/5900790741\n[14:00 - 16:50] Кроссплатформенная разработка мобильных приложений(А)\nhttps://us04web.zoom.us/j/2412177647\n[14:00 - 16:50] Oracle Database 11 g администрирование(Б)\nhttps://us04web.zoom.us/j/7621644476"

b = "[10:00 - 11:50] Oracle Database 11 g администрирование(л)\nhttps://us04web.zoom.us/j/2412177647?pwd=N0RhNmJWRThobkQ5KzVxVlUzdUZiUT09\n[12:00 - 12:50] Комплексное обеспечение безопасности инормационных систем(спз)\nhttps://us04web.zoom.us/j/9115674856"

c = "[12:00 - 13:50] Кроссплатформенная разработка мобильных приложений(л)\nhttps://us04web.zoom.us/j/2412177647\n[14:00 - 15:50] Комплексное обеспечение безопасности инормационных систем(спз)\nhttps://us04web.zoom.us/j/9115674856"

d = "[10:00 - 12:50] Методика научных исследований(спз)\nhttps://us04web.zoom.us/j/4313587454"

e = "[11:00 - 13:50] Oracle Database 11 g администрирование(А)\nhttps://us04web.zoom.us/j/7621644476\n[11:00 - 13:50] Кроссплатформенная разработка мобильных приложений(Б)\nhttps://us04web.zoom.us/j/2412177647\n[14:00 - 15:50] Методика научных исследований(л)\nhttps://us04web.zoom.us/j/5514039723"

token = os.environ.get('bot_token');
bot = telebot.TeleBot(str(token));

@bot.message_handler(commands=['start', 'help', 'papa'])
def start_1(message):
	if message.text == '/help':
		bot.send_message(message.from_user.id, 'При повторном запросе можно сразу забивать день недели.\nЕсли это только знакомство стоит прописать команду /start для знакомства с ботом');
	elif message.text == '/start':
		bot.send_message(message.from_user.id, 'Для работы с ботом поприветствую его!\n(Привет, привет, салам, хай)');
	elif message.text == '/papa':
		bot.send_message(message.from_user.id, 'Папа этого бота студент группы ИС-1705\nБарков Вадим');

@bot.message_handler(content_types=['text'])
def start(message):
	if message.text == 'привет' or message.text == 'Привет' or message.text == 'салам' or message.text == 'хай':
		keyboard = types.InlineKeyboardMarkup(); #наша клавиатура
		key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes'); #кнопка «Да»
		keyboard.add(key_yes); #добавляем кнопку в клавиатуру
		key_no= types.InlineKeyboardButton(text='Нет', callback_data='no');
		keyboard.add(key_no);
		question = 'Привет, хочешь узнать расписание?';
		bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)
	elif message.text == 'понедельник' or message.text == "Понедельник" or message.text == "пн" or message.text == "Пн":
		bot.send_message(message.from_user.id, a)
	elif message.text == 'Кто создатель?' or message.text == "кто создатель?":
		bot.send_message(message.from_user.id, "Для того, чтоб узнать создателя бота - воспользуйтесь командой /papa ")
	elif message.text == 'вторник' or message.text == "Вторник" or message.text == "вт" or message.text == "Вт":
		bot.send_message(message.from_user.id, b)
	elif message.text == 'среда' or message.text == "Среда" or message.text == "ср" or message.text == "Ср":
		bot.send_message(message.from_user.id, c)
	elif message.text == 'пятница' or message.text == "Пятница" or message.text == "пт" or message.text == "Пт":
		bot.send_message(message.from_user.id, e)
	elif message.text == 'четверг' or message.text == "Четверг" or message.text == "чт" or message.text == "Чт":
		bot.send_message(message.from_user.id, d)
	elif message.text == 'суббота' or message.text == "Суббота" or message.text == "Воскресенье" or message.text == "воскресенье":
		bot.send_message(message.from_user.id, "Выходной день! Отдыхай!")
	else:
		bot.send_message(message.from_user.id, 'Извини, я тебя не понимаю. Напиши /start');

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
		if call.data == "yes":
			...
			bot.send_message(call.message.chat.id, 'Введи день недели: ')

		else:
			...
			bot.send_message(call.message.chat.id, 'Ну как хочешь! Твое право отказаться :)')


bot.polling(none_stop=True, interval=0)
