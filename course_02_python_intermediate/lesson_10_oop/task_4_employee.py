"""
    📌 Создайте класс Сотрудник.
    📌 Воспользуйтесь классом человека из прошлого задания.
    📌 У сотрудника должен быть:
        ○ шестизначный идентификационный номер
        ○ уровень доступа вычисляемый как остаток от деления суммы цифр id на семь
"""

from task_3_person import Person, Gender
from random import randint

class Employee(Person):
    MAGIC_NUMBER = 7
    MIN_ID = 100_000
    MAX_ID = 999_999

    def __init__(self, name: str, patr_name: str, last_name: str, age: int, gender: Gender, emp_id: int):
        super().__init__(name, patr_name, last_name, age, gender)
        if self.MIN_ID <= emp_id <= self.MAX_ID:
            self.emp_id = emp_id
        else:
            self.emp_id = randint(self.MIN_ID, self.MAX_ID+1)

    def get_level(self)->int:
        return sum(int(n) for n in str(self.emp_id)) % self.MAGIC_NUMBER


if __name__ == '__main__':
    empl_1 = Employee('Bob', '----', 'Johnson', 45, Gender.male, 777_778)
    print(empl_1.get_level())   
    empl_2 = Employee('Bob', '----', 'Johnson', 45, Gender.male, 777_778)
    print(empl_2.get_level())   
    print(f'{hash(empl_1)=}, {hash(empl_2)=}')  
     