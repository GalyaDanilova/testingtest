import requests
import random
import telebot

from bs4 import BeautifulSoup as b

API_KEY = '6302041965:AAG48gZLT8UEM21jrpCxB18xOSi6_AXJQSk'
bot = telebot.TeleBot(API_KEY)
@bot.message_handler(content_types=['text'])
def talk(message):
    bot.send_message(message.chat.id, message.text)

bot.polling(none_stop=True)
