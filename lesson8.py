# # # class Person(object):
# # #
# # #     city = 'Minsk'
# # #     # all = []
# # #
# # #     # 1 step - создание объекта
# # #     # def __new__(cls, *args, **kwargs):
# # #     #     return cls()
# # #
# # #     # 2 step - конструктор
# # #     def __init__(self, name, email, age):
# # #         self.age = age
# # #         self.email = email
# # #         self.name = name.title()
# # #         self._i = -1
# # #         # self.all.append(self)
# # #
# # #     def __str__(self):
# # #         return f'User: name={self.name} email={self.email}'
# # #
# # #     def __len__(self):
# # #         return len(self.email)
# # #
# # #     def __getitem__(self, item):
# # #         return self.__getattribute__(item)
# # #
# # #     def __gt__(self, other):
# # #         if isinstance(other, Person):
# # #             return self.age > other.age
# # #         elif isinstance(other, (int, float)):
# # #             return self.age > other
# # #         else:
# # #             raise TypeError
# # #
# # #     def __add__(self, other):
# # #         if isinstance(other, Person):
# # #             return self.age + other.age
# # #         elif isinstance(other, int):
# # #             return self.age + other
# # #         else:
# # #             raise TypeError
# # #
# # #     def __radd__(self, other):
# # #         return self.__add__(other)
# # #
# # #     # def info(self):
# # #     #     return f'{self.email=} {self.name=} {self.city=}'
# # #
# # #     @classmethod
# # #     def change_city(cls, new_city):
# # #         cls.city = new_city.title()
# # #
# # #     # @classmethod
# # #     # def all_info(cls):
# # #     #     for user in cls.all:
# # #     #         print(user.name)
# # #
# # #     def __iter__(self):
# # #         return self
# # #
# # #     def __next__(self):
# # #         # try:
# # #         #     self.__getattribute__('_key')
# # #         # except:
# # #         #     self.__setattr__('_key', ['name', 'email', 'age'])
# # #         #
# # #         # if self._key:
# # #         #     key = self._key[0]
# # #         #     del self._key[0]
# # #         #     return self.__getattribute__(key)
# # #         # else:
# # #         #     del self._key
# # #         #     raise StopIteration
# # #         self._i += 1
# # #         if self._i < len(self.name):
# # #             return self.name[self._i]
# # #         else:
# # #             self._i = -1
# # #             raise StopIteration
# # #
# # #
# # # vasya = Person(name='vasya', email='vasya@info.com', age=34)
# # # petya = Person('petya', 'petya@info.com', 34)
# # # # print(vasya)
# # # # text = str(vasya)
# # # # print(text)
# # # # Person.change_city('SPB')
# # # # print(Person.city)
# # # # Person.all_info()
# # # # print(len(vasya))
# # # # print(vasya['name'])
# # #
# # # for val in vasya:
# # #     print(val)
# #
# # class Student:
# #
# #     def __init__(self, first_name: str, group: int, marks: list[int]) -> None:
# #         self.first_name = first_name
# #         self.group = group
# #         self.marks = marks
# #
# #     # def __str__(self) -> str:
# #     #     return f'Student: {self.first_name=} {self.group=} {self.marks=}'
# #
# #     @staticmethod
# #     def student_sort(student: list['Student']) -> list['Student']:
# #         student.sort(key=lambda x: x.first_name)
# #         return student
# #
# #
# # vasya = Student('vasya', 2, [3, 4, 3, 6])
# # petya = Student('petya', 4, [7, 6, 8])
# # masha = Student('masha', 1, [9, 8, 6, 5])
# # students = [vasya, petya, masha]
# # students = Student.student_sort(students)
# #
# # for student in students:
# #     print(student.first_name)
# from collections import Counter
#
#
# class Numbers:
#     def __init__(self, numbers: list[int]) -> None:
#         self.numbers = numbers
#
#     def average(self, numbers: list[int] = None) -> float:
#         """Нахождение среднего арифмитического списка чисел
#
#         :param numbers: список чисел
#         :return: среднее арифмитическое чисел
#         """
#         if numbers is None:
#             return sum(self.numbers) / len(self.numbers)
#         else:
#             return sum(numbers) / len(numbers)
#
#     def max_count(self) -> float:
#         from collections import Counter
#         numbers_counter = Counter(self.numbers)
#         max_count_number = numbers_counter.most_common(n=1)[0][1]
#         numbers = list(filter(lambda x: self.numbers.count(x) == max_count_number, self.numbers))
#         return self.average(numbers)
#
#
class User(object):

    def __init__(self, name, email, password):
        self.name = name.title()
        self.email = email
        self.__password = password

    @property
    def password(self):
        return self.__password[-4:]

    @password.setter
    def password(self, value):
        if len(value) >= 8:
            self.__password = value
        else:
            raise ValueError

    def get_password(self):
        return self.__password[-4:]

    def set_password(self, value):
        if len(value) >= 8:
            self.__password = value
        else:
            raise ValueError

    def __str__(self):
        return f'User: name={self.name} email={self.email}'

    def foo(self):
        print('foo')
#
#
# class Manager(User):
#
#     def __init__(self, name, email, password, salary):
#         super().__init__(name, email, password)
#         self.salary = salary
#
#     def __str__(self):
#         # text = super().__str__()
#         # text += f' salary={self.salary}'
#         # return text
#         return f'Manager: name={self.name} email={self.email} salary={self.salary}'
#
#
# vasya = User('vasya', 'vasya@info.com', 'password')
# print(vasya.get_password())
# vasya.set_password()
# print(vasya.password)
# vasya.password = 'qwertyuy'
# print(vasya.password)
#
#
# class Cat:
#
#     def say(self):
#         print('meow')
#
#
# class Dog:
#
#     def say(self):
#         print('woof')
#
#
# cat = Cat()
# dog = Dog()
#
#
# def say(obj: Cat | Dog):
#     obj.say()


class Button:

    def __init__(self, text: str, color: str):
        self.text = text
        self.color = color
        self.is_pressed = False

    def press(self):
        self.is_pressed = not self.is_pressed

    def __str__(self):
        return f'{self.text} {self.is_pressed}'


buttons = [
    Button(
        text=f'button {i}',
        color='red'
    )
    for i in range(1, 11)
]


class Keyboard:

    def __init__(self, buttons: list[Button]):
        self.buttons = buttons

    def press(self, button_numbers: list[int]):
        for button in self.buttons:
            if int(button.text[-1]) in button_numbers:
                button.press()

    def info(self):
        for button in self.buttons:
            print(button)


# keyboard = Keyboard(buttons)
# keyboard.press([2, 4, 6])
# keyboard.press([1, 2, 5])
# keyboard.info()


class Category(object):

    categories: list[str] = []

    @classmethod
    def add(cls, category: str) -> int:
        if category.title() not in cls.categories:
            cls.categories.append(category.title())
            return cls.categories.index(category.title())
        raise ValueError('argument `category` is not unique')

    @classmethod
    def get(cls, i: int) -> str:
        try:
            return cls.categories[i]
        except IndexError as e:
            raise ValueError(e)

    @classmethod
    def delete(cls,  i: int) -> None:
        # VAR 1
        if i in range(len(cls.categories)):
            del cls.categories[i]
        # VAR 2
        # try:
        #     del cls.categories[i]
        # except IndexError:
        #     pass

    @classmethod
    def update(cls, i: int, category: str) -> None:
        if i not in range(len(cls.categories)):
            cls.add(category)
        elif category.title() not in cls.categories:
            cls.categories[i] = category.title()
        else:
            raise ValueError('argument `category` is not unique')


from abc import ABC, abstractmethod


class Button(ABC):

    def __init__(self, text, color):
        self.text = text
        self.color = color

    def __str__(self):
        return f'{self.text} {self.color}'

    @abstractmethod
    def serialize(self, fields: list[str]) -> dict:
        pass


def __init__(self, text, color):
    self.text = text
    self.color = color


def __str__(self):
    return f'{self.text} {self.color}'


MetaButton = type('Button', (), {'__init__': __init__, '__str__': __str__})

meta_button = MetaButton(text='meta', color='black')
print(meta_button)
