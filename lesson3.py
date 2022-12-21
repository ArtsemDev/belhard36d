# is_human = True
# print(type(is_human))
#
# print(True + True)
# a = int(True)

# age = 43
# print(bin(age))
# print(age.bit_count())
# print(age.bit_length())
# print(age.to_bytes(length=4, byteorder='little'))
# print(age.as_integer_ratio())

# a = 0.2
# print(a.as_integer_ratio())

# a = float('nan')
# print(type(a))

# text = 'hello\'world'
# print(text)
# text = r'hello\nworld'
# print(text)

# age = 43
# name = 'Alex'
# text1 = 'Hello ' + name + ' your age ' + str(age)
# text2 = 'Hello %s your age %d' % (name, age)
# text3 = 'Hello {} your age {}'.format(name, age)
# text4 = f'Hello {name} your age {age}'
# print(text1)
# print(text2)
# print(text3)
# print(text4)

# text = 'hello world python pycharm'
# words = text.split()
# text = ' | '.join(words)
# print(text)
# print(words)

# text = 'hello WORLD python world pycharm β'
# print(text.partition('world'))
# print(text.rpartition('world'))
# print(text.count(' ', 6, 10))
# print(text.find(' '))
# print(text.rfind(' '))
# print(text.replace('world', 'hi', 1))
# print(text.startswith('wor', 6))
# print(text.endswith('hon', 6, 18))
# print(text.upper())
# print(text.lower())
# print(text.title())
# print(text.capitalize())
# print(text.swapcase())
# print(text.casefold())

# text = 'hello\tworld\tpython'
# text2 = 'java\tide\tjetbrains'
# print(text.expandtabs(12))
# print(text2.expandtabs(12))

# text = ' \t\thello\tpython\t\t\t'
# print(text.lstrip())
# print(text.rstrip())
# print(text.strip())

# text = 'hello python'
# print(text.removeprefix('hell'))
# print(text.removesuffix('hon'))
# text = "außen"
# print(text.casefold())

# text = 'world'
# print(text.ljust(10, '-'))
# print(text.rjust(10, '-'))
# print(text.center(4, '-'))
# print(text.zfill(10))
# a = 12
# print(bin(a)[2:].zfill(8))
# text = 'привет'

# print(4 // 2)
# print(4 // 2.0)

# a = 5.0
# print(a.is_integer())

# print(bin(12))
# print(bin(14))
# print(12 & 14)
# print(12 | 14)
# print(12 ^ 14)
# print(~4)
# print(~-15)
# print(2 << 3)
# print(bin(2))
# print(bin(16))
# print(bin(14))
# print(bin(3))
# print(14 >> 2)
# text = '56'
# text2 = '550'
# print(text > text2)
# print(5 == 5.0)

# text = 'hello world python pycharm'
# print('Python' not in text)

# a = 0.4
# b = (a / 4) * 4
# print(id(a))
# print(id(b))
# print(b)
# print(a == b)

# пользователь вводит строку с клавиатуры состоящая минимум из 3х слов
#  переставить местами первое и последнее слово с строке
text = 'hello world python'
first_word = text[:text.find(' ')]
last_word = text[text.rfind(' ')+1:]
center = text[text.find(' '):text.rfind(' ')+1]
text = last_word + center + first_word

