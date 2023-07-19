"""
    ✔ Функция получает на вход список чисел и два индекса.
    ✔ Вернуть сумму чисел между между переданными индексами.
    ✔ Если индекс выходит за пределы списка, сумма считается
    до конца и/или начала списка.
"""

def calc_sum_between_indexes(arr: [int], start: int, end: int) -> int:
    if start > end:
        start, end = end, start
    if start < 0: start = 0 
    if end > len(arr) - 1: end = len(arr) - 1
    return sum(arr[start:end+1]) 

print(calc_sum_between_indexes([1,2,3,4,5,6], 4, 1))