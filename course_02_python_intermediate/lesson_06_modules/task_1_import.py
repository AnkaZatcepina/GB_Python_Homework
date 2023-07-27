"""
    Вспомните какие модули вы уже проходили на курсе. 
    Создайте файл, в котором вы импортируете встроенные в модуль функции под псевдонимами. (3-7 строк импорта).
"""
from random import randint as rnd
from sys import getsizeof as size
from math import sqrt as sq

print(rnd(1, 100))
x = [1,2]
print(size(x))
print(sq(100))