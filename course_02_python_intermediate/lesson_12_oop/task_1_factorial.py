"""
    📌 Создайте класс-функцию, который считает факториал числа при
    вызове экземпляра.
    📌 Экземпляр должен запоминать последние k значений.
    📌 Параметр k передаётся при создании экземпляра.
    📌 Добавьте метод для просмотра ранее вызываемых значений и
    их факториалов.
"""
from collections import deque

class Factorial:
    def __init__(self, k:int):
        self._history = deque(maxlen=k)

    def __call__(self, number:int):
        mul_num = 1
        for i in range(2, number + 1):
            mul_num *= i
        self._history.append({number: mul_num})
        return mul_num

    def get_history(self):
        return self._history  

if __name__ == '__main__':
    fact_1 = Factorial(2) 
    print(fact_1(5))
    print(fact_1(10))
    print(fact_1(15))
    print(fact_1.get_history())             