
import telebot
from telebot import types
import requests
import json
token = '5298893897:AAEwZXoX8oAc5XkZYTLWnLcb8_bvhbd3iEQ'

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def welcome(message):
	keyboard = telebot.types.InlineKeyboardMarkup()
	profile = types.InlineKeyboardButton(text = 'Мой профиль', callback_data ='prof')
	help = types.InlineKeyboardButton(text = 'Админ', url="https://t.me/Azqazqazqazqazq")
	how = types.InlineKeyboardButton(text = 'Как работает бот?', callback_data ='kak')
	keyboard.add(how)
	keyboard.add(profile, help) 
	bot.send_message(message.chat.id, f'Привет {message.from_user.first_name} я бот который может пробить IP-адрес.\nВведи IP в формате: 8.8.8.8', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def cll(call):
	if call.data == 'prof':
		bot.send_message(call.message.chat.id, f'Name: {call.message.chat.first_name}\nUsername: @{call.message.chat.username}\nID: {call.message.chat.id}')
	elif call.data == 'kak':
		bot.send_message(call.message.chat.id, 'Бот отправляет запрос сайту для получение информации и затем отправляет информацию вам')


@bot.message_handler(content_types=['text'])
def text(message):
	ipp = message.text
	bot.send_message(message.chat.id, "Ищу информацию, подождите несколько секунд")
	url = 'https://ipapi.co/' + ipp + '/json/'
	try:
		json = requests.get(url).json()
		bot.send_message(message.chat.id, f'''Публичный IP-адрес: {json["ip"]}
Город: {json["city"]}
Регион: {json["region"]}
Код региона: {json["region_code"]}
Страна: {json["country"]}
Название страны: {json["country_name"]}
Столица страны: {json["country_capital"]}
Широта: {json["latitude"]}
Долгота: {json["longitude"]}
Часовой пояс: {json["timezone"]}
Валюта: {json["currency"]}
Название валюты: {json["currency_name"]}
Насиление страны: {json["country_population"]}
Поставщик/Провайдер: {json["org"]}'''
)
	except:
		bot.send_message(message.chat.id, 'Неверный IP-адрес или произошла ошибка')

bot.polling()
