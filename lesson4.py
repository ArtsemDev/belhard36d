# # # # # # # # # # # # # # # # # # # words = ['hello', 'python', 'world']
# # # # # # # # # # # # # # # # # # # print(words[1][2])
# # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # text = 'hello world python'
# # # # # # # # # # # # # # # # # # # words = text.split()
# # # # # # # # # # # # # # # # # # # print(words)
# # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # text = 'words'
# # # # # # # # # # # # # # # # # # lst = list(text)
# # # # # # # # # # # # # # # # # # print(lst)
# # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # numbers = [i*2 for i in range(1, 100)]
# # # # # # # # # # # # # # # # # print(numbers)
# # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # print(list(range(1, 101, 2)))
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # words = ['hello', 'python', 'world']
# # # # # # # # # # # # # # # del words[1:]
# # # # # # # # # # # # # # # print(words)
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # words = ['hello', 'python', 'world', 'python']
# # # # # # # # # # # # # # words.remove('python')
# # # # # # # # # # # # # # words.remove('python')
# # # # # # # # # # # # # # # words.remove('python')
# # # # # # # # # # # # # # # print(words)
# # # # # # # # # # # # # # # word = words.pop(1)
# # # # # # # # # # # # # # # print(word)
# # # # # # # # # # # # # # # print(words)
# # # # # # # # # # # # #
# # # # # # # # # # # # #
# # # # # # # # # # # # # lst = [1, 2, 3, 4]
# # # # # # # # # # # # # lst.extend('hello')
# # # # # # # # # # # # # lst.append([5, 6])
# # # # # # # # # # # # # # lst.insert(1, 'new')
# # # # # # # # # # # # # print(lst)
# # # # # # # # # # # #
# # # # # # # # # # # # numbers = [4, 5, 2, 5, 3, 78, 3, 6, -6, 2, -89]
# # # # # # # # # # # # numbers.sort(reverse=True)
# # # # # # # # # # # # print(numbers)
# # # # # # # # # # #
# # # # # # # # # # # words = ['hello', 'Python', 'world', 'python', 'age', 'hell']
# # # # # # # # # # # words.sort()
# # # # # # # # # # # print(words)
# # # # # # # # # # # words.sort(key=len)
# # # # # # # # # # # print(words)
# # # # # # # # # #
# # # # # # # # # # numbers = [1, 2, 3, 4]
# # # # # # # # # # numbers.reverse()
# # # # # # # # # # print(numbers[::-1])
# # # # # # # # # # print(numbers)
# # # # # # # # #
# # # # # # # # # numbers = [1, 2, 3, 4, 5]
# # # # # # # # # numbers.clear()
# # # # # # # #
# # # # # # # # # lst = [1, 2, 3, 4]
# # # # # # # # # lst2 = [5, 6, 7]
# # # # # # # # # lst2.append(lst)
# # # # # # # # # lst2[3].append(0)
# # # # # # # # # lst.append(9)
# # # # # # # # # print(lst2)
# # # # # # # # # print(lst)
# # # # # # # #
# # # # # # # # # words = ['hello', 'python', 'world']
# # # # # # # # # words[1] = 'PYTHON'
# # # # # # # # # print(words)
# # # # # # # #
# # # # # # # # # numbers = [1, 2, 3, 4]
# # # # # # # # # numbers2 = list(numbers)
# # # # # # # #
# # # # # # # # numbers = [1, 2, 3, 4]
# # # # # # # # numbers2 = [5, 6, 7]
# # # # # # # # numbers += numbers2
# # # # # # # # print(numbers * 2)
# # # # # # #
# # # # # # # numbers = [1, 2, 3, 4]
# # # # # # # numbers2 = [1, 2, 4]
# # # # # # # print(numbers2 > numbers)
# # # # # #
# # # # # # # numbers = (1, )
# # # # # # # print(numbers)
# # # # # #
# # # # # # numbers = 1, 2, 3, 4, 5
# # # # # # print(numbers)
# # # # #
# # # # # # numbers = [1, 2, 3, 4, 5]
# # # # # # tup = (numbers, 6, 7, 8)
# # # # # # tup[0].append(6)
# # # # # # print(tup)
# # # # #
# # # # # # user = {
# # # # # #     'name': 'Alex',
# # # # # #     'age': 43,
# # # # # #     'city': 'Minsk',
# # # # # #     'languages': ['ru', 'en']
# # # # # # }
# # # # # # user['name'] = 'Pavel'
# # # # # # user['key'] = 'value'
# # # # # # print(len(user))
# # # # #
# # # # # # user = dict([('name', 'alex'), ('age', 43)])
# # # # # # print(user)
# # # # #
# # # # # letters = {i: i*2 for i in 'hello'}
# # # # # print(letters)
# # # #
# # # # user = dict.fromkeys(('name', 'age', 'city'), 'value')
# # # # print(user)
# # #
# # #
# # # user = {
# # #     'name': 'alex',
# # #     'age': 34
# # # }
# # # print(user.get('city', 'Н/У'))
# # # print(user.setdefault('city', 'Н/У'))
# # # print(user)
# # # del user['age']
# # # print(user)
# # # value = user.pop('lang', 'Н/У')
# # # print(value)
# # # print(user.popitem())
# # # print(user)
# # # print(list(user.keys()))
# # # print(list(user))
# # # print(user.values())
# # # print(user.items())
# #
# #
# user = {
#     'name': 'alex',
#     'age': 34
# }
# print('alex' in user.values())
# # new_data = {
# #     'age': 35,
# #     'city': 'minsk'
# # }
# # # user.update(new_data)
# # # print(user)
# # new_user = user | new_data
# # print(new_user)
# # print(user)
# # print(new_data)

# words = 'hello python'
# s = set(words)
# print(s)

# s1 = {1, 2, 3, 4}
# s1.add(5)
# print(s1)
# s2 = {2, 3, 5, 6, 7, 8}
# print(s2.isdisjoint(s1))
# print(s2.issubset(s1))
# print(s1.issuperset(s2))
# print(s2 <= s1)
# print(s1 >= s2)
# print(s1.union(s2))
# print(s1 | s2 | {9, 8, 0, -15})
# print(s2.difference(s1))
# print(s2 - s1)
# print(s1.intersection(s2))
# print(s1 & s2)
# print(s1 ^ s2)
# print(s2.symmetric_difference(s1))
# print(s1 | s2)
# s1 |= s2
# s1.update(s2)
# print(s1)
# s1 &= s2 & {3, 2, 4}
# print(s1)
# s1 = {1, 2, 3, 4}
# s1 = frozenset(s1)
# s1 = set(s1)
# print(s1)
from collections import Counter


# words = ('python', 'python', 'hello', 'world', 'hello', 'hello')
# words2 = ('world', 'hello', 'world', 'hello', 'hello', 'hello')
# words_counter = Counter(words)
# words_counter2 = Counter(words2)
# print(words_counter)
# print(words_counter2)
# words_counter2.subtract(words_counter)
# print(words_counter2)
# print(words_counter.most_common(1))
# print(list(words_counter.elements()))
# from collections import deque
# numbers = [1, 2, 3, 4, 5]
# q = deque(numbers, 2)
# print(q)

# from collections import OrderedDict, namedtuple, ChainMap
# from collections import *
# data = defaultdict(list)
# data['languages'].append('ru')
# print(data)
# user = OrderedDict({'name': 'alex', 'age': 34, 'city': 'minsk'})
# user.move_to_end('age', last=False)
# print(user)

# User = namedtuple('User', ('name', 'age', 'city'))
# vasya = User('vasya', 34, 'minsk')
# print(vasya)
# print(vasya.city)
# print(vasya._asdict())

# data = {'a': 4, 'b': 5}
# data2 = {'c': 6, 'b': 3}
# chain = ChainMap(data, data2)
# chain['c'] = 8
# print(chain)


