"""
Телеграм-бот с сохранением информации о пользователях.
Лото с номерами дипломатических машин и мигалок АМР97
"""

from telebot import TeleBot
import time

# считываем файл с данными пользователей
ud_file = open("userdata.txt", "w+")

bot = TeleBot()

bot.polling()
