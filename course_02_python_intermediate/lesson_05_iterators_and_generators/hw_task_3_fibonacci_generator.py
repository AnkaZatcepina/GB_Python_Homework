#Создайте функцию генератор чисел Фибоначчи
def fibonacci_generator(n:int):
    previous:int = 0
    current: int = 1
    for i in range(1, n + 1):
        if i == 1:
            yield previous
        elif i == 2:
            yield current
        else:
            result = previous + current
            previous, current = current, result
            yield result


for n in fibonacci_generator(15):
    print(n, end=' ')