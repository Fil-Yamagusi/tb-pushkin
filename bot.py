#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
    2023-12-14 @Fil
    Телеграм-бот Визитка Александра Сергеевича
    Fil FC Визитка Пушкина
    fil_fc_pushkin_bot
    6886396528:AAHO-KXXB5NS63pKaBAnIIh1wkPrEPd10X8
    https://t.me/fil_fc_pushkin_bot
"""

import time
import random
import re
from urllib.parse import quote
from urllib.request import Request, urlopen

from telebot import TeleBot
from telebot.types import ReplyKeyboardMarkup, Message
from answers import *


random.seed(time.time())

TOKEN = "6886396528:AAHO-KXXB5NS63pKaBAnIIh1wkPrEPd10X8"
bot = TeleBot(TOKEN)

markup = ReplyKeyboardMarkup(
    row_width=2,
    resize_keyboard=True)
markup.add(* ["❓ Расскажи о себе",
              "🖼 Скинь фотку",
              "✍ Как делишки?",
              "👶 Как детишки?",
              "✴️ Поделись клёвой рифмой?",
              "🆘 ПАМАГИТЕ"])


# Здороваемся, говорим кратко о возможностях бота
@bot.message_handler(
    func=lambda message:
    any(word in message.text.lower()
        for word in ['памаги', 'помоги', 'помощ', 'ыефке', 'руддщ', 'рудз']),
    content_types=["text"])
@bot.message_handler(
    commands=["start", "hello", "help"])
def handle_start(message: Message):
    """ Функция с подсказками """
    bot.send_message(
        message.chat.id,
        "Привѣтъ, " +
        message.chat.first_name +
        "! 🤝\nЯ - виртуальный Пушкинъ.\n"
        "Со всѣмъ уваженіемъ къ настоящему!\n\n"
        "Могу немного разсказать о себѣ /about\n"
        "Вот-съ свѣжія дагеротипы изъ салона /photo\n"
        "Новости о дѣлахъ насущныхъ /dela\n"
        "Охотно подѣлюсь новостями о дѣтяхъ /deti\n"
        "Могу подѣлиться знатной риѳмой /rhyme\n\n"
        "Вспомнить cии повелнiя: /help",
        reply_markup=markup
    )


# Краткая биография великого поэта. Спасибо нейросети
@bot.message_handler(
    func=lambda message:
    any(word in message.text.lower()
        for word in ['о себе', 'кто ты']),
    content_types=["text"])
@bot.message_handler(
    commands=["about"])
def handle_about(message: Message):
    """ Функция с биографией поэта """
    for phrase in answers_pushkin:
        bot.send_message(
            message.chat.id,
            phrase,
            parse_mode="HTML",
            reply_markup=markup)


# Оправляем фотку Пушкина
@bot.message_handler(
    func=lambda message:
    any(word in message.text.lower()
        for word in ['фото', 'фотк', 'картин']),
    content_types=["text"])
@bot.message_handler(commands=["photo"])
def handle_photo(message: Message):
    """ Функция со случайными фото """
    ext = ['.webp', '.jpg'][random.randint(0, 1)]
    with open(f"photo/{random.randint(1, 25)}{ext}", 'rb') as photo:
        bot.send_photo(
            message.chat.id,
            photo,
            caption=get_answers_photo(),
            reply_markup=markup
        )


# Случайная новость о делах Пушкина. Подгружается из списка во внешнем файле
@bot.message_handler(
    func=lambda message:
    any(word in message.text.lower()
        for word in ['дела', 'делиш', 'вудф']),
    content_types=["text"])
@bot.message_handler(commands=["dela"])
def handle_dela(message: Message):
    """ Функция со случайными делами (типа твиты) """
    bot.send_message(
        message.chat.id,
        get_answers_dela() +
        "\n\n<i>За творческие новости спасибо нейросети.</i>",
        parse_mode="HTML",
        reply_markup=markup)


# Случайный факт о детях Пушкина. Подгружается из списка во внешнем файле
@bot.message_handler(
    func=lambda message:
    any(word in message.text.lower()
        for word in ['дети', 'детя', 'детк', 'вуеш']),
    content_types=["text"])
@bot.message_handler(commands=["deti"])
def handle_deti(message: Message):
    """ Функция со случайными фразочками о детях """
    bot.send_message(
        message.chat.id,
        get_answers_deti() +
        "\n\n<i>Кстати, это факты от нейросети! Ошибка на ошибке!</i>",
        parse_mode="HTML",
        reply_markup=markup)


# Случайная прикольная рифма. Подгружается из списка во внешнем файле
@bot.message_handler(
    func=lambda message:
    any(word in message.text.lower()
        for word in ['рифм', 'зарифм', 'крнь']),
    content_types=["text"])
@bot.message_handler(commands=["rhyme"])
def handle_rhyme(message: Message):
    """ Функция со случайными рифмами """
    bot.send_message(
        message.chat.id,
        get_answers_rhyme(),
        parse_mode="HTML",
        reply_markup=markup)


# Для наставника
@bot.message_handler(commands=["description"])
def handle_description(message: Message):
    """ Функция с пояснениями для наставника """
    bot.send_message(
        message.chat.id,
        "Кроме команд, бот ответит и на сообщения. Например:\n"
        "/start = /hello = /help = "
        "['памаги', 'помоги', 'ыефке', 'руддщ', 'рудз']\n"
        "/about = ['о себе', 'кто ты']\n"
        "/photo = ['фото', 'фотк', 'картин']\n"
        "/dela = ['дела', 'делиш', 'вудф']\n"
        "/deti = ['дети', 'детя', 'детк', 'вуеш']\n"
        "/rhyme = ['рифм', 'зарифм', 'крнь']\n\n"
        "Бот может показать не тот раздел, если несколько ключевых слов найдёт"
        " во фразе, зато на словоформы и простые опечатки старается ответить:\n"
        "<i>зарифмуй чё-нить?</i>\n"
        "<i>что делаешь?</i>\n"
        "<i>расскажи о семье, о детях?</i>\n",
        parse_mode="HTML",
        reply_markup=markup)


# Тут пытаюсь подобрать рифмы. Но вдруг нам дают русские слова без рифм?
@bot.message_handler(
    func=lambda message:
    any(word in message.text.lower()
        for word in [
            'туловище', 'жаворонок', 'восемьдесят', 'выхухоль',
            'заморозки', 'набережная', 'пользователь', 'проволока']),
    content_types=["text"])
def handle_no_rhymes(message: Message):
    """ Редкая функция: хвалим настойчивых искателей рифм """
    bot.send_message(
        message.chat.id,
        "Сударь или сударыня!\n\n"
        "Поражён вашей настойчивостью или удачей!\n"
        "Вы предлагаете мне найти рифму к слову, которое по мнению "
        "некоторых поэтов вообще не имеет достойной рифмы!\n\n"
        "Так держать! Во славу русской поэзии! Deus vult!",
        parse_mode="HTML",
        reply_markup=markup)


# Обработка невыясненных команд
@bot.message_handler(content_types=["text"])
def handle_error(message: Message):
    """ Функция с ответом на абсолютно непонятные фразы пользователя """
    words = message.text.lower().split()
    has_russian_word = False
    find_word = ""
    vowels = list('аяуюоёэеыи')

    for word in reversed(words):
        if len(word) < 3:
            continue
        if not any(char in vowels for char in word):
            continue
        if bool(re.fullmatch(r'(?i)[а-яё ]+', word)):
            has_russian_word = True
            find_word = word
            break

    if has_russian_word:
        bot.reply_to(
            message,
            f"{find_word}, {find_word}... хмм...\n"
            f"Попробую зарифмовать! Где моя тетрадь с рифмами...",
            parse_mode="HTML",
            reply_markup=markup)

        url = "https://rifmovka.ru/rifma/{0}#similar".format(quote(find_word))
        # print(url)
        request_site = Request(url, headers={"User-Agent": "Mozilla/5.0"})
        try:
            webpage = urlopen(request_site).read().decode('utf-8')
            webpage = re.sub(r'<b>', '', webpage)
            webpage = re.sub(r'</b>', '', webpage)
            # pattern = "<meta name=\"description\" content=\"(.*): (.*)\">"
            pattern = r'<li class="vis [a-z]+" data-id="\d+">(.+)</li>'
            match = re.findall(pattern, webpage)

            if match:
                rhymes = match
                for r in rhymes:
                    if len(r) > 12:
                        rhymes.remove(r)
                random.shuffle(rhymes)
                rhymes = rhymes[0:7]
                answ = f"Зацени рифмы: <b>{find_word}</b> - {', '.join(rhymes)}"
            else:
                answ = f"Не могу найти рифму к слову <b>{find_word}</b> 🧐"

            bot.send_message(
                message.chat.id,
                answ,
                parse_mode="HTML",
                reply_markup=markup)

        except Exception as ex:
            print(ex)
    else:
        bot.send_message(
            message.chat.id,
            "Mon ami, je ne te comprends pas!\n\n"
            "Помощь тебе в помощь! /help",
            parse_mode="HTML",
            reply_markup=markup)


print(TOKEN)
while True:
    try:
        bot.polling(none_stop=True)
    except Exception as ex:
        print(ex)
        time.sleep(5)
