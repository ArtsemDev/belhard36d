# # # # # # # from re import compile, Pattern
# # # # # # #
# # # # # # #
# # # # # # # email_re = compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
# # # # # # from itertools import *
# # # # # #
# # # # # #
# # # # # # products = ['coffee', 'tea', 'donut', 'milk', 'eggs', 'bread', 'bear']
# # # # # # products = iter(products)
# # # # # # print(list(zip_longest(products, products)))
# # # # # # from math import *
# # # # #
# # # # # # print(sqrt(4))
# # # # # # print(ceil(2.1))
# # # # # # print(floor(3.9))
# # # # # # print(factorial(8))
# # # # # # from random import *
# # # # # # print(triangular(1, 10, 3))
# # # # #
# # # # # # from os import system, mkdir
# # # # # # mkdir('folder')
# # # # # # system('shutdown -r')
# # # # #
# # # # # from pathlib import Path
# # # # # from os.path import join
# # # # # from os import getenv
# # # # # import os
# # # # #
# # # # #
# # # # # BASE_DIR = Path(__file__).resolve().parent
# # # # # UTILS_DIR = join(BASE_DIR, 'utils')
# # # # # print(UTILS_DIR)
# # # #
# # # # from datetime import datetime, date, time, timedelta, timezone
# # # #
# # # # now = datetime.now()
# # # # # print(now.strftime('%a %d %B %y %H:%M'))
# # # # # print(datetime.strptime('Wed 18 January 23 12:02', '%a %d %B %y %H:%M'))
# # # # # print(now.timestamp())
# # # # # print(datetime.fromtimestamp(1674032389.859844))
# # # # delta = timedelta(days=5)
# # # # print(now + delta)
# # # from dataclasses import dataclass
# # #
# # #
# # # # from dataclasses import dataclass
# # # #
# # # #
# # # # @dataclass
# # # # class User:
# # # #     name: str
# # # #     email: str
# # # #     age: int
# # # #     city: str = None
# # # #
# # # #
# # # # class MyUser:
# # # #
# # # #     def __init__(self, name, email, age, city):
# # # #         self.name = name
# # # #         self.email = email
# # # #         self.age = age
# # # #         self.city = city
# # # #
# # # #     def __str__(self):
# # # #         return f"User(name='{self.name}', email='{self.email}', age={self.age}, city={self.city})"
# # # #
# # # #
# # # # vasya = User(name='vasya', email='vasya@info.com', age=23)
# # # # petya = User(name='petya', email='petya@info.com', age=24)
# # # # print(vasya)
# # # # print(petya.email)
# # #
# # # from enum import Enum, IntEnum
# # #
# # #
# # # # class Role(int, Enum):
# # # #     Admin: int = 1
# # # #     Manager: int = 2
# # # #     User: int = 3
# # #
# # # # Role = IntEnum('Role', (('Admin', 1), ('Manager', 2), ('User', 3)))
# # # #
# # # #
# # # # @dataclass
# # # # class User:
# # # #     name: str
# # # #     role_id: int
# # # #
# # # #
# # # # vasya = User('vasya', 1)
# # # #
# # # #
# # # # if vasya.role_id == Role.Admin:
# # # #     print('admin')
# # #
# # # from argparse import ArgumentParser
# # #
# # # parser = ArgumentParser()
# # # parser.add_argument(
# # #     '-p',
# # #     '--port',
# # #     default=8000
# # # )
# # # parser.add_argument(
# # #     '-d',
# # #     '--debug',
# # #     action='store_true'
# # # )
# # # args = parser.parse_args()
# # # print(args)
# # import logging
# #
# # logging.basicConfig(
# #     filename='log.log',
# #     filemode='a',
# #     format='[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s',
# #     level=logging.INFO
# # )
# #
# #
# # logging.error('Error, User Stupid!')
# # logging.info('INFO')
#
#
# #  TODO Написать Класс KeyboardButton, на вход конструктора поступают аргументы:
# #   text: str, request_contact: bool, request_location: bool
# #   Перед определением атрибутов объекта на основании аргументов, произвести валидацию
# #   значение аргументов по типу данных
# #   Написать метод объекта dict возвращающий словарь с атрибутами объекта и из значениями
#
# #  TODO Написать класс KeyboardMarkup, констурктор класса принимает аргументы:
# #   keyboard: list[list[KeyboardButton]], resize_keyboard: bool, one_time_keyboard: bool
# #   Перед определением атрибутов объекта на основании аргументов, произвести валидацию
# #   значение аргументов по типу данных
# #   Написать магический serialize возвращающий представление объекта в виде словаря
# #   с атрибутами и их значениями, пример:
# #   {'resize_keyboard': True, 'one_time_keyboard': False, 'keyboard': [[{'text': 'Button1',
# #   'request_contact': False, 'request_location': False}]]
#
#
# class KeyboardButton:
#
#     def __init__(self, text: str,  request_contact: bool = False, request_location: bool = False) -> None:
#         if not isinstance(text, str):
#             raise TypeError('argument `text` must be string')
#         if not isinstance(request_contact, bool):
#             raise TypeError('argument `request_contact` must be boolean')
#         if not isinstance(request_location, bool):
#             raise TypeError('argument `request_location` must be boolean')
#         if request_contact and request_location:
#             raise ValueError
#
#         self.text = text
#         self.request_contact = request_contact
#         self.request_location = request_location
#
#     def dict(self) -> dict:
#         return {
#             'text': self.text,
#             'request_contact': self.request_contact,
#             'request_location': self.request_location
#         }
#
#
# class KeyboardMarkup:
#
#     def __init__(
#             self,
#             keyboard: list[list[KeyboardButton]],
#             resize_keyboard: bool = True,
#             one_time_keyboard: bool = False
#     ) -> None:
#         if not isinstance(resize_keyboard, bool):
#             raise TypeError('argument `resize_keyboard` must be boolean')
#         if not isinstance(one_time_keyboard, bool):
#             raise TypeError('argument `one_time_keyboard` must be boolean')
#         if not isinstance(keyboard, list):
#             raise TypeError('argument `keyboard` must be list')
#         for line in keyboard:
#             if not isinstance(line, list):
#                 raise TypeError
#             for button in line:
#                 if not isinstance(button, KeyboardButton):
#                     raise TypeError
#
#         self.keyboard = keyboard
#         self.resize_keyboard = resize_keyboard
#         self.one_time_keyboard = one_time_keyboard
#
#     def serialize(self) -> dict:
#         return {
#             'resize_keyboard': self.resize_keyboard,
#             'one_time_keyboard': self.one_time_keyboard,
#             'keyboard': [
#                 list(map(lambda x: x.dict(), line))
#                 for line in self.keyboard
#             ]
#         }
#
#
# markup = KeyboardMarkup(
#     keyboard=[
#         [
#             KeyboardButton(text='button1'),
#             KeyboardButton(text='button2'),
#         ],
#         [
#             KeyboardButton(text='button3'),
#             KeyboardButton(text='button4'),
#         ]
#     ]
# )
#
# numbers = [-4, 23, 4, 3, -6, -45]
# result = []
# for number in numbers:
#     if number >= 0:
#         result.append(number ** 0.5)
#     else:
#         result.append(number ** 2)
#
# numbers = list(map(lambda x: x ** 0.5 if x >= 0 else x ** 2, numbers))
