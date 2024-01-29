"""
Поиск дубликатов

Реализовать с использованием функциональной парадигмы процедуру для поиска дубликатов. На вход
подается массив, где могут присутствовать дубликаты (а могут и не присутствовать). При применении к
массиву, дубликаты должны быть выведены на экран в виде списка.

"""

def find_duplicates(numbers):
    unique_numbers = set()
    return list(filter(lambda x: x in unique_numbers or unique_numbers.add(x), numbers))

numbers = [1,2,3,2,4,5,3,6,6,2]
duplicates = find_duplicates(numbers)
print(duplicates)