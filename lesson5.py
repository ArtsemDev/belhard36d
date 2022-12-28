# # # # # # # # # # # # # value = input()
# # # # # # # # # # # # # if value.isdigit():
# # # # # # # # # # # # #     value = int(value)
# # # # # # # # # # # # #     print(type(value))
# # # # # # # # # # # #
# # # # # # # # # # # # number = int(input())
# # # # # # # # # # # #
# # # # # # # # # # # # if number % 2:
# # # # # # # # # # # #     print('odd')
# # # # # # # # # # # #     print('odd')
# # # # # # # # # # # #     print('odd')
# # # # # # # # # # # # elif number == 0:
# # # # # # # # # # # #     print('zero')
# # # # # # # # # # # #     print('zero')
# # # # # # # # # # # #     print('zero')
# # # # # # # # # # # # else:
# # # # # # # # # # # #     print('even')
# # # # # # # # # # # #     print('even')
# # # # # # # # # # # #     print('even')
# # # # # # # # # # # #
# # # # # # # # # # # # number = '123456'
# # # # # # # # # # # #
# # # # # # # # # # # # if not number.isdigit():
# # # # # # # # # # # #     print('digit')
# # # # # # # # # # #
# # # # # # # # # # #
# # # # # # # # # # # number = 23
# # # # # # # # # # # is_even = 'No' if number % 2 else 'Yes' if number != 0 else 'Zero'
# # # # # # # # # # #
# # # # # # # # # # # if number % 2:
# # # # # # # # # # #     is_even = 'No'
# # # # # # # # # # # else:
# # # # # # # # # # #     if number != 0:
# # # # # # # # # # #         is_even = 'Yes'
# # # # # # # # # # #     else:
# # # # # # # # # # #         is_even = 'Zero'
# # # # # # # # # # #
# # # # # # # # # # # print('No' if number % 2 else 'Yes')
# # # # # # # # # #
# # # # # # # # # # # number = 56
# # # # # # # # # # #
# # # # # # # # # # # if number % 17 or (number > 0 and not number % 2):
# # # # # # # # # #
# # # # # # # # # #
# # # # # # # # # # x = True
# # # # # # # # # # y = False
# # # # # # # # # # z = False
# # # # # # # # # # if not x or y:
# # # # # # # # # #     print(1)
# # # # # # # # # # elif not x or not y and z:
# # # # # # # # # #     print(2)
# # # # # # # # # # elif not x or y or not y and x:
# # # # # # # # # #     print(3)
# # # # # # # # # # else:
# # # # # # # # # #     print(4)
# # # # # # # # #
# # # # # # # # # # for number in range(1, 10, 2):
# # # # # # # # # #     number **= 2
# # # # # # # # # #     print(number)
# # # # # # # # #
# # # # # # # # # # text = 'hello world'
# # # # # # # # # # for elem in text:
# # # # # # # # # #     elem = elem.upper()
# # # # # # # # # #     print(elem)
# # # # # # # # # # for i in range(len(text)):
# # # # # # # # # #     print(text[i])
# # # # # # # # # # for i, j in enumerate(text):
# # # # # # # # # #     print(i)
# # # # # # # # #
# # # # # # # # # # data = [
# # # # # # # # # #     [1, 2, 3],
# # # # # # # # # #     [4, 5, 6],
# # # # # # # # # #     [7, 8, 9]
# # # # # # # # # # ]
# # # # # # # # # # for i, j, k in data:
# # # # # # # # # #     print(i, j, k)
# # # # # # # # #
# # # # # # # # # data = {
# # # # # # # # #     'key1': 'value1',
# # # # # # # # #     'key2': 'value2',
# # # # # # # # #     'key3': 'value3',
# # # # # # # # #     'key4': 'value4',
# # # # # # # # # }
# # # # # # # # #
# # # # # # # # # # for key in data:
# # # # # # # # # #     print(key)
# # # # # # # # # # for value in data.values():
# # # # # # # # # #     print(value)
# # # # # # # # # for key, val in data.items():
# # # # # # # # #     print(key, val)
# # # # # # # # words = ['word1', 'word2', 'word3', 'word4']
# # # # # # # #
# # # # # # # # # for i in range(len(words)):
# # # # # # # # #     del words[i]
# # # # # # # #
# # # # # # # # for elem in words:
# # # # # # # #     if elem.startswith('w'):
# # # # # # # #         words.remove(elem)
# # # # # # # # print(words)
# # # # # # #
# # # # # # # for i in range(1, 100, 2):
# # # # # # #     if i % 5 == 0:
# # # # # # #         continue
# # # # # # #     print(i)
# # # # # #
# # # # # # for i in range(1, 100, 2):
# # # # # #     if i == 16:
# # # # # #         break
# # # # # #     print(i)
# # # # # # else:
# # # # # #     print('finish')
# # # # # # print('exit')
# # # # #
# # # # # a = 2
# # # # # while a < 1024:
# # # # #     a *= 2
# # # # # print(a)
# # # #
# # # # # Вводится число, посчитать сумму его цифр
# # # # # number = '123'
# # # # # s = 0
# # # # # for el in number:
# # # # #     s += int(el)
# # # # # print(s)
# # # #
# # # # # # Пользователь дурак, необходимо спрашивать данные с клавиатуры до тех пор
# # # # # #  пока пользователь не введет число
# # # # # number = input('enter number, please: ')
# # # # # while not number.isdigit():
# # # # #     number = input('are you stupid? try again: ')
# # # # # print(number)
# # # # # while not (number := input('enter digit: ')).isdigit(): ...
# # # # # TOD# # # # # # # # # # value = input()
# # # # # # # # # # # # # # if value.isdigit():
# # # # # # # # # # # # # #     value = int(value)
# # # # # # # # # # # # # #     print(type(value))
# # # # # # # # # # # # #
# # # # # # # # # # # # # number = int(input())
# # # # # # # # # # # # #
# # # # # # # # # # # # # if number % 2:
# # # # # # # # # # # # #     print('odd')
# # # # # # # # # # # # #     print('odd')
# # # # # # # # # # # # #     print('odd')
# # # # # # # # # # # # # elif number == 0:
# # # # # # # # # # # # #     print('zero')
# # # # # # # # # # # # #     print('zero')
# # # # # # # # # # # # #     print('zero')
# # # # # # # # # # # # # else:
# # # # # # # # # # # # #     print('even')
# # # # # # # # # # # # #     print('even')
# # # # # # # # # # # # #     print('even')
# # # # # # # # # # # # #
# # # # # # # # # # # # # number = '123456'
# # # # # # # # # # # # #
# # # # # # # # # # # # # if not number.isdigit():
# # # # # # # # # # # # #     print('digit')
# # # # # # # # # # # #
# # # # # # # # # # # #
# # # # # # # # # # # # number = 23
# # # # # # # # # # # # is_even = 'No' if number % 2 else 'Yes' if number != 0 else 'Zero'
# # # # # # # # # # # #
# # # # # # # # # # # # if number % 2:
# # # # # # # # # # # #     is_even = 'No'
# # # # # # # # # # # # else:
# # # # # # # # # # # #     if number != 0:
# # # # # # # # # # # #         is_even = 'Yes'
# # # # # # # # # # # #     else:
# # # # # # # # # # # #         is_even = 'Zero'
# # # # # # # # # # # #
# # # # # # # # # # # # print('No' if number % 2 else 'Yes')
# # # # # # # # # # #
# # # # # # # # # # # # number = 56
# # # # # # # # # # # #
# # # # # # # # # # # # if number % 17 or (number > 0 and not number % 2):
# # # # # # # # # # #
# # # # # # # # # # #
# # # # # # # # # # # x = True
# # # # # # # # # # # y = False
# # # # # # # # # # # z = False
# # # # # # # # # # # if not x or y:
# # # # # # # # # # #     print(1)
# # # # # # # # # # # elif not x or not y and z:
# # # # # # # # # # #     print(2)
# # # # # # # # # # # elif not x or y or not y and x:
# # # # # # # # # # #     print(3)
# # # # # # # # # # # else:
# # # # # # # # # # #     print(4)
# # # # # # # # # #
# # # # # # # # # # # for number in range(1, 10, 2):
# # # # # # # # # # #     number **= 2
# # # # # # # # # # #     print(number)
# # # # # # # # # #
# # # # # # # # # # # text = 'hello world'
# # # # # # # # # # # for elem in text:
# # # # # # # # # # #     elem = elem.upper()
# # # # # # # # # # #     print(elem)
# # # # # # # # # # # for i in range(len(text)):
# # # # # # # # # # #     print(text[i])
# # # # # # # # # # # for i, j in enumerate(text):
# # # # # # # # # # #     print(i)
# # # # # # # # # #
# # # # # # # # # # # data = [
# # # # # # # # # # #     [1, 2, 3],
# # # # # # # # # # #     [4, 5, 6],
# # # # # # # # # # #     [7, 8, 9]
# # # # # # # # # # # ]
# # # # # # # # # # # for i, j, k in data:
# # # # # # # # # # #     print(i, j, k)
# # # # # # # # # #
# # # # # # # # # # data = {
# # # # # # # # # #     'key1': 'value1',
# # # # # # # # # #     'key2': 'value2',
# # # # # # # # # #     'key3': 'value3',
# # # # # # # # # #     'key4': 'value4',
# # # # # # # # # # }
# # # # # # # # # #
# # # # # # # # # # # for key in data:
# # # # # # # # # # #     print(key)
# # # # # # # # # # # for value in data.values():
# # # # # # # # # # #     print(value)
# # # # # # # # # # for key, val in data.items():
# # # # # # # # # #     print(key, val)
# # # # # # # # # words = ['word1', 'word2', 'word3', 'word4']
# # # # # # # # #
# # # # # # # # # # for i in range(len(words)):
# # # # # # # # # #     del words[i]
# # # # # # # # #
# # # # # # # # # for elem in words:
# # # # # # # # #     if elem.startswith('w'):
# # # # # # # # #         words.remove(elem)
# # # # # # # # # print(words)
# # # # # # # #
# # # # # # # # for i in range(1, 100, 2):
# # # # # # # #     if i % 5 == 0:
# # # # # # # #         continue
# # # # # # # #     print(i)
# # # # # # #
# # # # # # # for i in range(1, 100, 2):
# # # # # # #     if i == 16:
# # # # # # #         break
# # # # # # #     print(i)
# # # # # # # else:
# # # # # # #     print('finish')
# # # # # # # print('exit')
# # # # # #
# # # # # # a = 2
# # # # # # while a < 1024:
# # # # # #     a *= 2
# # # # # # print(a)
# # # # #
# # # # # # Вводится число, посчитать сумму его цифр
# # # # # # number = '123'
# # # # # # s = 0
# # # # # # for el in number:
# # # # # #     s += int(el)
# # # # # # print(s)
# # # # #
# # # # # # # Пользователь дурак, необходимо спрашивать данные с клавиатуры до тех пор
# # # # # # #  пока пользователь не введет число
# # # # # # number = input('enter number, please: ')
# # # # # # while not number.isdigit():
# # # # # #     number = input('are you stupid? try again: ')
# # # # # # print(number)
# # # # # # while not (number := input('enter digit: ')).isdigit(): ...
# # # # # # дан список чисел, необходимо удалить из списка чисел все 2
# # # # # numbers = [4, 2, 6, 3, 6, 2, 8, 5, 8, 2, 6, 2, 5, 2, 2, 2, 2, 6]
# # # # # # # while 2 in numbers:
# # # # # # #     numbers.remove(2)
# # # # # for _ in range(8):
# # # # #     numbers.remove(2)
# # # # #
# # # # # # print(a, b, _)O дан список чисел, необходимо удалить из списка чисел все 2
# # # # numbers = [4, 2, 6, 3, 6, 2, 8, 5, 8, 2, 6, 2, 5, 2, 2, 2, 2, 6]
# # # # # # while 2 in numbers:
# # # # # #     numbers.remove(2)
# # # # for _ in range(8):
# # # #     numbers.remove(2)
# # # #
# # # # # numbers = (4, 9, 2)
# # # # # a, b, _ = numbers
# # # # # print(a, b, _)
# # #
# # # try:
# # #     a = int(input())
# # #     b = int(input())
# # #     c = a / b
# # # except ValueError:
# # #     print('введено не число')
# # # except ZeroDivisionError:
# # #     print('на 0 делить нельзя')
# # # except Exception as e:
# # #     print(e)
# # #     print('все остальные')
# # # else:
# # #     print('ошибок не было')
# # # finally:
# # #     print("выполнится в любом случае")
# # # number = input()
# # # if number.isdigit():
# # #     number = int(number)
# # # else:
# # #     raise ValueError('you stupid?')
# #
# #
# # # for i in range(10):
# # #     print(i)
# # #     for j in 'hello':
# # #         print(j)
# #
# #
# # # Вводится число N, вывести максимальную степень числа 2 в которая не превышает N
# # #  прим: N = 34, ответ 5 т.к 2**5=32
# # N = 34
# # i = 0
# # while 2 ** i <= N:
# #     i += 1
# # i -= 1
# # print(i)
# #
# #  написать калькулятор вклада капитализации:
# #  Вводится сумма вклада и процент вклада, сказать через сколько лет вклад удвоится
# #  (вклад капитализации)
# deposit = 100
# target = deposit * 2
# percent = 0.1
# percent += 1
# year = 0
# while deposit < target:
#     deposit *= percent
#     year += 1
# print(year)
