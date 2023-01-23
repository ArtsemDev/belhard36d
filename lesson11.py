# # # # from pathlib import Path
# # # #
# # # #
# # # # BASE_DIR = Path(__file__).resolve().parent
# # # #
# # # # # with (
# # # # #     open(BASE_DIR.joinpath('input.txt'), mode='r', encoding='utf-8') as file,
# # # # #     open('output.txt', 'r') as file2
# # # # # ):
# # # # #     print(file.readline())
# # # # #     print(file2.readline())
# # # #
# # # #
# # # # #
# # # # # # file = open(BASE_DIR.joinpath('input.txt'), mode='r', encoding='utf-8')
# # # # # # print(BASE_DIR.joinpath('input.txt'))
# # # # #
# # # # # # print(file.read())
# # # # # # print(file.readline())
# # # # # # print(file.readlines())
# # # # #
# # # # # # lines = [line.strip() for line in file if line.strip()]
# # # # # # file.seek(4)
# # # # # # print(file.readline())
# # # # # # file.close()
# # # # # file = open('output.txt', 'a', encoding='utf-8')
# # # # # file.write('Hello world!\nPython!')
# # # # # # file.writelines(['hello world!\n', 'java'])
# # # # # file.close()
# # # #
# # # # from json import load, loads, dump, dumps
# # # #
# # # #
# # # # # with open('user.json', 'r', encoding='utf-8') as file:
# # # # #     data = load(file)
# # # # # # print(data)
# # # # #
# # # # # text = '''{
# # # # #   "name": "Vasya",
# # # # #   "age": 45,
# # # # #   "is_human": true,
# # # # #   "city": null,
# # # # #   "languages": ["en", "ru"]
# # # # # }'''
# # # # # print(loads(text))
# # # #
# # # # user = {
# # # #     'name': 'петя',
# # # #     'city': 'Minsk',
# # # #     'is_human': True
# # # # }
# # # #
# # # # with open('new_user.json', 'w') as file:
# # # #     dump(user, file, indent=2, ensure_ascii=False)
# # # from datetime import datetime
# # #
# # # from pydantic import BaseModel, Field, EmailStr, validator, root_validator
# # # from pydantic.types import Decimal
# # #
# # # emails = ('alex@info.com', 'pavel@info.com')
# # #
# # #
# # # class Passport(BaseModel):
# # #     serial: str = Field(min_length=2, max_length=2)
# # #     number: str = Field(min_length=7, max_length=7)
# # #
# # #
# # # class User(BaseModel):
# # #     username: str = Field(min_length=4, max_length=64)
# # #     age: int = Field(ge=18, lt=100)
# # #     is_human: bool = Field(default=True)
# # #     email: EmailStr
# # #     passport: Passport
# # #     date_of_birth: datetime
# # #
# # #     @validator('email')
# # #     def email_validator(cls, value: str) -> str:
# # #         if value.lower() not in emails:
# # #             return value.lower()
# # #         else:
# # #             raise ValueError('argument `email` is not unique')
# # #
# # #     @validator('date_of_birth', pre=True)
# # #     def dof_validator(cls, value):
# # #         if isinstance(value, (int, float)):
# # #             return datetime.fromtimestamp(value)
# # #         elif isinstance(value, str):
# # #             value = float(value)
# # #             return datetime.fromtimestamp(value)
# # #         raise TypeError('argument `date_of_birth` must be integer or floating point')
# # #
# # #     @root_validator()
# # #     def root(cls, values: dict) -> dict:
# # #         if values.get('username').lower() not in values.get('email').lower():
# # #             raise ValueError('email does not contain username')
# # #         return values
# # #
# # #
# # # user = {
# # #     'username': 'Alex',
# # #     'age': 32,
# # #     'email': 'alex2@info.com',
# # #     'date_of_birth': 727769709,
# # #     'passport': {
# # #         'serial': 'KB',
# # #         'number': '1234567'
# # #     }
# # # }
# # #
# # #
# # # user = User(**user)
# # # print(user.date_of_birth.year)
# #
# #
# # from csv import reader, DictReader, writer, DictWriter
# #
# #
# # with open('users.csv', 'r', encoding='utf-8') as file:
# #     # r = reader(file)
# #     # for user in r:
# #     #     print(user)
# #     r = DictReader(file, delimiter='|')
# #     for user in r:
# #         print(user)
# #
# # # with open('users.csv', 'a', encoding='utf-8') as file:
# # #     # w = writer(file)
# # #     # w.writerow(['\nmisha', '23', 'brest'])
# # #     w = DictWriter(file, fieldnames=('name', 'age', 'city'))
# # #     w.writerow({'name': 'misha', 'age': '23', 'city': 'brest'})
# from pandas import DataFrame as df
#
#
# frame = df(
#     {
#         'name': ['vasya', 'petya'],
#         'age': [32, 23]
#     }
# )
# frame.to_excel('users.xlsx', sheet_name='users', index=False)

from yaml import load, dump, FullLoader, safe_load


with open('input.yaml', 'r', encoding='utf-8') as file:
    data = load(file, FullLoader)
print(data)
#
# user = {
#     'username': 'Alex',
#     'age': 32,
#     'email': 'alex2@info.com',
#     'is_human': True,
#     'city': None,
#     'languages': ['ru', 'en']
# }
# with open('output.yaml', 'w', encoding='utf-8') as file:
#     dump(user, file)
