"""
    📌 Напишите класс для хранения информации о человеке:
    ФИО, возраст и т.п. на ваш выбор.
    📌 У класса должны быть методы birthday для увеличения
    возраста на год, full_name для вывода полного ФИО и т.п. на
    ваш выбор.
    📌 Убедитесь, что свойство возраст недоступно для прямого
    изменения, но есть возможность получить текущий возраст.
"""
from enum import Enum

class Gender(Enum):
    male = 'male'
    female = 'female'

class Person:
    def __init__(self, name: str, patr_name: str, last_name: str, age: int, gender: Gender):
        self.name = name
        self.patr_name = patr_name
        self.last_name = last_name
        self.gender = gender
        self._age = age
    def birthday(self)->None:
        self._age += 1
    def get_full_name(self)->str:
        return f'{self.last_name} {self.name} {self.patr_name}'
    def get_age(self)->int:
        return self._age

if __name__ == '__main__':
    oleg = Person('Олег', 'Петрович', 'Смирнов', 45, Gender.male)
    print(oleg.get_age())      
    oleg.birthday()     
    print(oleg.get_age())  
    print(oleg.get_full_name())           