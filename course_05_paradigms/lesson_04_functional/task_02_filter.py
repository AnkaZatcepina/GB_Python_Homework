"""
Фильтрация данных

Написать скрипт принимающий на вход массив с данными о людях и число - возраст, а возвращающий
число - количество людей старше указанного возраста.

"""

people = [
    {'name': 'Elizaveta', 'age': 25},
    {'name': 'Vasiliy', 'age': 30},
    {'name': 'Sergey', 'age': 35},
    {'name': 'Ivan', 'age': 40},
]

def filter_by_age(people: list, min_age: int) -> list:
    return list(filter(lambda x: x['age'] > min_age, people))

print(len(filter_by_age(people,29)))
