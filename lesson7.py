from typing import Any


def binary_search(objs, target):
    start = 0
    end = len(objs)
    i = (end + start) // 2
    while objs[i] != target:
        if objs[i] > target:
            end = i
        elif objs[i] < target:
            start = i
        i = (end + start) // 2
    return i


def decimal_to_binary(decimal):
    binary = ''
    while decimal > 0:
        binary = f'{decimal % 2}' + binary
        decimal //= 2
    binary = f'{decimal}' + binary
    return binary


def binary_to_decimal(binary):
    decimal = 0
    for i in binary:
        decimal *= 2
        decimal += int(i)
    return decimal


def encode_morse(text):
    text = text.upper()
    morse_dict = {
        'A': '.-',
        'B': '-...',
        'C': '-.-.',
        'D': '-..',
        'E': '.',
        'F': '..-.',
        'G': '--.',
        'H': '....',
        'I': '..',
        'J': '.---',
        'K': '—.—',
        'L': '.—..',
        'M': '--',
        'N': '-.',
        'O': '---',
        'P': '.--.',
        'Q': '--.-',
        'R': '.-.',
        'S': '...',
        'T': '-',
        'U': '..-',
        'V': '...-',
        'W': '.--',
        'X': '-..-',
        'Y': '-.--',
        'Z': '--..',
        '1': '.----',
        '2': '..---',
        '3': '...--',
        '4': '....-',
        '5': '.....',
        '6': '-....',
        '7': '--...',
        '8': '---..',
        '9': '----.',
        ' ': ' '
    }
    morse = ''
    for el in text:
        morse += morse_dict.get(el, '')
        if el in morse_dict:
            morse += ' '
    return morse


def decode_morse(morse):
    morse = morse.replace('   ', ' | ')
    text = ''
    morse_dict = {
        'A': '.-',
        'B': '-...',
        'C': '-.-.',
        'D': '-..',
        'E': '.',
        'F': '..-.',
        'G': '--.',
        'H': '....',
        'I': '..',
        'J': '.---',
        'K': '—.—',
        'L': '.—..',
        'M': '--',
        'N': '-.',
        'O': '---',
        'P': '.--.',
        'Q': '--.-',
        'R': '.-.',
        'S': '...',
        'T': '-',
        'U': '..-',
        'V': '...-',
        'W': '.--',
        'X': '-..-',
        'Y': '-.--',
        'Z': '--..',
        '1': '.----',
        '2': '..---',
        '3': '...--',
        '4': '....-',
        '5': '.....',
        '6': '-....',
        '7': '--...',
        '8': '---..',
        '9': '----.',
        ' ': '|'
    }
    morse_dict = dict(zip(morse_dict.values(), morse_dict.keys()))
    morse = morse.split()
    for el in morse:
        text += morse_dict.get(el, '')
    return text


def shift_list(objs, shift):
    if abs(shift) > len(objs):
        shift -= (shift // len(objs)) * len(objs)
    objs = objs[-shift:] + objs[:-shift]
    return objs


# elements = [1, 2, 3, 'ertyu', 'wertyu', 34, 'ertyu']
# res = list(filter(lambda x: isinstance(x, str), elements))
# print(res)


def string_filter(objs):
    for i in range(len(objs) - 1, -1, -1):
        if not isinstance(objs[i], str):
            del objs[i]
    return objs


def reverse(objs: list[Any]):
    for i in range(len(objs) // 2):
        objs[i], objs[~i] = objs[~i], objs[i]
    return objs


# numbers = [4, 5, 23, 6, 23, 76, 23, 5, 3, 5, 23, 45, 2, 43, 2]
# numbers.sort(key=lambda x: x % 2)
# print(numbers)


def sum_of_neighbors(numbers: list) -> list:
    result = []
    for i in range(len(numbers)):
        # var 1
        # if i < len(numbers) - 1:
        #     result.append(numbers[i-1] + numbers[i+1])
        # else:
        #     result.append(numbers[i-1] + numbers[0])
        # var 2
        result.append(numbers[i-1] + numbers[i - len(numbers) + 1])
    return result


# TODO На вход функции поступает простейшая химическая формула, например C2H5OH
#  вернуть словарь где ключами выспупают название элементов, а значение: колличество
#  моллекул данного вещества ({"C": 2, "H": 6, "O": 1})


def elements_count(formula: str) -> dict[str, int]:
    formula += '1' if formula[-1].isalpha() else ''
    formula = list(formula)
    i = 0
    while i < len(formula) - 1:
        if formula[i].isalpha() and formula[i+1].isalpha():
            formula.insert(i+1, '1')
            i += 1
        i += 1
    # formula = list(map(lambda x: int(x) if x.isdigit() else x, formula))
    data = {}
    for i in range(0, len(formula), 2):
        if formula[i] not in data:
            data[formula[i]] = int(formula[i+1])
        else:
            data[formula[i]] += int(formula[i+1])
    return data


def get_cabinet_area(x1, y1, x2, y2, x3, y3, x4, y4):
    max_x = max(x1, x2, x3, x4)
    min_x = min(x1, x2, x3, x4)
    max_y = max(y1, y2, y3, y4)
    min_y = min(y1, y2, y3, y4)
    return max(max_x - min_x, max_y - min_y) ** 2


# TODO на вход функции поступает N целое положительное число
#  вернуть N первых простых чисел больших 0, в виде кортежа


def get_prime_numbers(n: int) -> tuple[int]:
    number = 2
    while n > 0:
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                break
        else:
            n -= 1
            yield number
        number += 1
