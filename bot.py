# -*- coding: utf8 -*-

import telebot
import os
from telebot import types

a = "[14:00 - 15:50] Интеллектульные информационные системы и базы знаний(л)\nhttps://us04web.zoom.us/j/6467674915?pwd=SmNYaUlBMGVTMlJ2ZVdsOTgvcG1yZz09\n[16:00 - 18:50] Кроссплатформенная разработка мобильных приложений (Б)\nhttps://us04web.zoom.us/j/5149248980?pwd=UFVyd3FjVnNEQ3BURkJSU3FrdWJxUT09"

b = "[11:00 - 13:50] Администрирование систем и сетей\nhttps://us04web.zoom.us/j/7621644476?pwd=d3daRUdJUml5WkFlcUErVytKZEczZz09\n[14:00 - 15:50] Распределенные информационные системы\nhttps://us04web.zoom.us/j/5900790741?pwd=NkZrUFJ0QXFQVUpERjN2Z1IyN2FwZz09"

c = "[10:00 - 11:50] Программирование в MS SQL (б)\nhttps://us04web.zoom.us/j/8636724102\n[12:00 - 14:50] Информационнные системы предприятия\nhttps://us04web.zoom.us/j/8635475529\n[15:00 - 16:50]Программирование в MS SQL (а)\nhttps://us04web.zoom.us/j/8636724102"

d = "[8:00 - 9:50] Программирование в MS SQL (б)\nhttps://us04web.zoom.us/j/8636724102\n[10:00 - 11:50] Информационнные системы предприятия\nhttps://us04web.zoom.us/j/8635475529\n[12:00 - 13:50]Программирование в MS SQL (а)\nhttps://us04web.zoom.us/j/8636724102"

e = "[пятница]"

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
