"""Реализуйте алгоритм перемешивания списка.
(рандомно поменять местами элементы списка между собой)"""

import random
list = [3, 5, 6, 7, 7796]
print(f"Изначальный список: {list}")
random.shuffle(list)
print(f"Перемешанный список: {list}")