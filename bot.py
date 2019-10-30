# -*- coding: utf8 -*-

import telebot
import os
from telebot import types

a = ("[8:00] IT Инфраструктура(А) / Численные методы в информационных системах(Б)\n[9:00] IT Инфраструктура(А) / Численные методы в информационных системах(Б)\n[10:00] IT Инфраструктура(А) / Численные методы в информационных системах(Б)")

b = ("[13:00] Основы цифровой миклоэлектронники(Б)\n[14:00] Язык программирования Python(A) / Основы цифровой миклоэлектронники(Б)\n[15:00] Язык программирования Python(A) / Основы цифровой миклоэлектронники(Б)\n[16:00] Язык программирования Python\n[17:00] Язык программирования Python\n[18:00] Кураторский час")

c = ("[8:00] Численный методы в информационных системах(А) / IT Инфраструктура(Б)\n[9:00] Численный методы в информационных системах(А) / IT Инфраструктура(Б)\n[10:00] Численный методы в информационных системах(А) / IT Инфраструктура(Б)\n[11:00] - \n[12:00] Основы цифровой миклоэлектронники\n[13:00] Основы цифровой миклоэлектронники\n[14:00] Численные методы в информационных системах\n[15:00] Численные методы в информационных системах")

d = ["[8:00] Основы цифровой миклоэлектронники(А) / Язык программирования Python(Б)\n[9:00] Основы цифровой миклоэлектронники(А) / Язык программирования Python(Б)\n[10:00] Основы цифровой миклоэлектронники(А) / Язык программирования Python(Б)\n[11:00] Язык программирования Python(A)\n[12:00] IT Инфраструктура\n[13:00] IT Инфраструктура"]

token = os.environ.get('bot_token')
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
	elif message.text == 'понедельник' or message.text == "Понедельник":
		bot.send_message(message.from_user.id, a)
	elif message.text == 'Кто создатель?' or message.text == "кто создатель?":
		bot.send_message(message.from_user.id, "Для того, чтоб узнать создателя бота - воспользуйтесь командой /papa ")
	elif message.text == 'вторник' or message.text == "Вторник":
		bot.send_message(message.from_user.id, b)
	elif message.text == 'среда' or message.text == "Среда":
		bot.send_message(message.from_user.id, c)
	elif message.text == 'пятница' or message.text == "Пятница":
		bot.send_message(message.from_user.id, d)
	elif message.text == 'четверг' or message.text == "Четверг":
		bot.send_message(message.from_user.id, "Военная кафедра!")
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
