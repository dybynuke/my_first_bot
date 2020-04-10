# -*- coding: utf8 -*-

import telebot
import os
from telebot import types

a = "[8:00 - 10:50] Программирование в MS SQL (б)\n [ID] 863-672-4102 \n [11:00] Кураторский час \n [ID] 754-207-7646 \n [12:00 - 13:50] Компьютерное и математическое моделирование \n [ID] 908-871-8956 \n [14:00 - 16:50] Компьютерное и математическое моделирование(а) \n [ID] 427-420-9111"

b = "[12:00 2506] Визуальное программирование\n[13:00 2506] Визуальное программирование\n[14:00 2506] Программирование микропроцессоров\n[15:00 2511/2520] Программирование микропроцессоров(а) / Разработка Web-приложений(б)\n[16:00 2511/2520] Программирование микропроцессоров(а) / Разработка Web-приложений(б)\n[17:00 2511/2520] Программирование микропроцессоров(а) / Разработка Web-приложений(б)\n[18:00 2511/2520] Программирование микропроцессоров(а) / Визуальное программирование(б)"

c = "[13:00 2506] Базы данных в ИС\n[14:00 2506] Базы данных в ИС\n[15:00 2504/2511] Базы данных в ИС(a) / Базы даных(б)\n[16:00 2504/2511] Базы данных в ИС(a) / Базы данных в ИС(б)\n[17:00 2504/2511] Базы данных в ИС(a) / Базы данных в ИС(б)"

d = "[14:00 2508/2520] Программирование микропроцессоров(б) / Визуальное программирование(а)\n[15:00 2508/2520] Программирование микропроцессоров(б) / Визуальное программирование(а)\n[16:00 2508/2520] Программирование микропроцессоров(б) / Визуальное программирование(а)\n[17:00 2508] Программирование микропроцессоров(б)"

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
		bot.send_message(message.from_user.id, d)
	elif message.text == 'четверг' or message.text == "Четверг" or message.text == "чт" or message.text == "Чт":
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
