"""
Телеграм-бот с сохранением информации о пользователях.
Лото с номерами дипломатических машин и мигалок АМР97
"""

from telebot import TeleBot
import time


class User:
    def __init__(self, uid: int):
        self.uid = uid
        self.name = ""
        self.age = 0

    def print(self):
        print(f"name = '{self.name}', age = {self.age}")


class UserData:
    def __init__(self):
        # словарь из пользователей в виде классов
        self.Users = {}
        pass

    def get_user_by_uid(self, uid: int):
        if uid in self.Users.keys():
            return self.Users[uid]
        else:
            return False

    def add_user(self, uid: int):
        if not self.get_user_by_uid(uid):
            new_user = User(uid)
            self.Users[uid] = new_user
            return uid
        else:
            return False

    def modify_user_name(self, uid: int, new_name: str):
        one_user = self.get_user_by_uid(uid)
        if not one_user:
            return False
        else:
            one_user.name = new_name
            return one_user


Lotto = UserData()
for i in range(5):
    Lotto.add_user(i)

# print(Lotto)
# print(Lotto.Users)
Lotto.get_user_by_uid(1).print()

for i in range(5):
    Lotto.modify_user_name(i, "Cake " + str(i ** 3))
    Lotto.get_user_by_uid(i).print()


#TODO считываем файл с данными пользователей, не удаляя содержимое




TOKEN = ""
# bot = TeleBot(TOKEN)

# bot.polling()
