# # # # # # # # number = input('enter: ')
# # # # # # # # # numbers = list(number)
# # # # # # # # # print(max(number))
# # # # # # # #
# # # # # # # # max_num = 0
# # # # # # # # for i in number:
# # # # # # # #     if int(i) > max_num:
# # # # # # # #         max_num = int(i)
# # # # # # # #
# # # # # # # # print(max_num)
# # # # # # #
# # # # # # # # c = 5
# # # # # # # #
# # # # # # # #
# # # # # # # def multiply(a, b=5, d=None):
# # # # # # #     if not d:
# # # # # # #         c = a * b
# # # # # # #         return c
# # # # # # #     else:
# # # # # # #         c = (a * b) // d
# # # # # # #         return c
# # # # # # # #
# # # # # # # #
# # # # # # # # res = multiply(3, 4)
# # # # # # # # print(multiply(d=6, a=4, b=8))
# # # # # # #
# # # # # # #
# # # # # # # def summ(*args):
# # # # # # #     s = 0
# # # # # # #     for i in args:
# # # # # # #         s += i
# # # # # # #     return s
# # # # # # #
# # # # # # #
# # # # # # # # print(summ(1, 2, 3, 2, 3, 2, 3, 2, 3, 2))
# # # # # # #
# # # # # # # def bar(**kwargs):
# # # # # # #     print(kwargs)
# # # # # # #
# # # # # # #
# # # # # # # # bar(name='alex', age=43, city='minsk')
# # # # # # #
# # # # # # #
# # # # # # # def baz(a, b, c=5, *args, d=None):
# # # # # # #     print(a)
# # # # # # #     print(b)
# # # # # # #     print(c)
# # # # # # #     print(args)
# # # # # # #     print(d)
# # # # # # #
# # # # # # #
# # # # # # # # baz(1, 2, 3, 4, 5, 6, 7, 8, 9, 0)
# # # # # # #
# # # # # # #
# # # # # # # def foo(a, b=None):
# # # # # # #     if b is None:
# # # # # # #         b = []
# # # # # # #     b.append(a)
# # # # # # #     return b
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # a = 5
# # # # # #
# # # # # # def bar():
# # # # # #     print('bar global')
# # # # # #
# # # # # # def foo():
# # # # # #     a = 4
# # # # # #     def bar():
# # # # # #         # a = 3
# # # # # #         print('bar local')
# # # # # #     bar()
# # # # #
# # # # #
# # # # # # multiply = lambda a, b: a * b
# # # # # #
# # # # # # print(multiply(4, 5))
# # # # #
# # # # # # def my_sort(x):
# # # # # #     return x if isinstance(x, int) else ord(x[0])
# # # # # #
# # # # # #
# # # # # # lst = [1, 2, 3, 2, 43, 2, 'asdfg', 'qwer', 2345, 'daf']
# # # # # # lst.sort(key=my_sort)
# # # # # # print(lst)
# # # # #
# # # # # words = ['Hello', 'python', 'apple', 'Abc']
# # # # # words.sort(key=lambda x: x.lower())
# # # # # # ['hello', 'python', 'apple', 'age']
# # # # # print(words)
# # # # # a = 5
# # # # # def foo():
# # # # #     a = 4
# # # # #     def bar():
# # # # #         nonlocal a
# # # # #         print(a)
# # # # #     bar()
# # # # # foo()
# # # #
# # # # # def foo():
# # # # #     print('foo')
# # # # #
# # # # # def bar():
# # # # #     print('bar')
# # # # #
# # # # #
# # # # # globals().get('foo')()
# # # #
# # # #
# # # # # numbers = ['1', '2', '3', '4', '5', '6']
# # # # # numbers = list(map(lambda x: int(x) ** 2, numbers))
# # # # # print(numbers)
# # # # # for i in range(len(numbers)):
# # # # #     numbers[i] = int(numbers[i])
# # # # #
# # # # # print(numbers)
# # # #
# # # # # numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# # # # # numbers = list(filter(lambda x: x % 2 == 0, numbers))
# # # # # print(numbers)
# # # #
# # # #
# # # # # numbers = [1, 2, 3, 4]
# # # # # text = 'hello'
# # # # # t = (True, False, None)
# # # # # res = list(zip(numbers, text, t))
# # # # # print(res)
# # # #
# # # # keys = ('name', 'age', 'city')
# # # # values = ('alex', 32, 'minsk')
# # # # data = dict(zip(keys, values))
# # # # print(data)
# # #
# # #
# # # # def foo(a):
# # # #     def bar(b):
# # # #         def baz(c):
# # # #             return a * b * c
# # # #
# # # #         return baz
# # # #
# # # #     return bar
# # # #
# # # #
# # # # res = foo(5)(4)(3)
# # # # print(res)
# # #
# # #
# # # # def multiply(a, b):
# # # #     return a * b
# # # #
# # # #
# # # # def foo(func, a, b):
# # # #     print(func(a, b))
# # #
# # #
# # # # foo(multiply, 6, 5)
# # #
# # #
# # # def foo():
# # #     print('foo')
# # #
# # #
# # # def bar():
# # #     print('bar')
# # #
# # #
# # # def error():
# # #     print('error')
# # #
# # #
# # # a = 3
# # # data = {
# # #     1: foo,
# # #     2: bar,
# # # }
# # # data.get(a, error)()
# #
# #
# # users = [
# #     ('alex', 32),
# #     ('pavel', 33),
# #     ('masha', 34),
# #     ('petya', 35),
# # ]
# #
# #
# # def get_users():
# #     for user in users:
# #         yield user
# #
# #
# # res = get_users()
# # for user in res:
# #     print(user)
# # # print(res)
# # # print(next(res))
# # # print(next(res))
# # # print(next(res))
# # # print(next(res))
# # # print(next(res))
#
# numbers = [2, 3, 4, 2, 4, 32, [4, 56, 3, 5, 32, 5, 3, [5, 3, 5, 3], 5, 3, [5, 3, 45, 3, 42, 4, 2, 4,2 ]], 5, 3, 5, [5, 3, 5, 3, [3, 5, 3, 4, [4, 2, 4, 2, 5]], 45, 3, 4, 4, 3, 4]]
#
#
# def recursive_multiply(numbers):
#     res = 1
#     for number in numbers:
#         if isinstance(number, (int, float)):
#             res *= number
#         elif isinstance(number, (list, tuple, set, frozenset)):
#             res *= recursive_multiply(number)
#     return res
#
#
# print(recursive_multiply(numbers))

# def foo(a):
#     def my_decorator(func):
#         def wrapper(*args):
#             args = list(args)
#             for i in range(len(args)):
#                 if not isinstance(args[i], (int, float)):
#                     raise TypeError
#                 args[i] += a
#             res = func(*args)
#             return f'{res=}'
#
#         return wrapper
#     return my_decorator
#
#
# @foo(2)
# def multiply(a, b):
#     return a * b
#
#
# print(multiply(4, 5))
# def dispatcher():
#     registry = []
#
#     def filters(**kwargs):
#         def wrapper(func):
#             registry.append({'func': func, 'filters': kwargs})
#
#             def decorator(**kwargs):
#                 return func(**kwargs)
#             return decorator
#         return wrapper
#     filters.all = registry
#     return filters
#
#
# dp = dispatcher()
#
#
# @dp(name='foo')
# def foo(name):
#     print(name)
#
#
# @dp(name='bar')
# def bar(name):
#     print(name)
#
#
# name = 'foo'
# for func in dp.all:
#     filters = {f'{name=}'.split('=')[0]: name}
#     for key, val in filters.items():
#         if func['filters'].get(key) != val:
#             break
#     else:
#         func['func'](name)


#  На вход функции, поступает строка, на ее основании сформировать и вернуть
#  список, который будет содержать только слова, длина которых >= 5

text = 'hello python world age hell dog pycharm'
#
# words = list(filter(lambda x: len(x) >= 5, text.split()))
# print(words)

def filter_words(text):
    words = text.split()
    for i in range(len(words) - 1, -1, -1):
        if len(words[i]) < 5:
            del words[i]
    return words


print(filter_words(text))

#
