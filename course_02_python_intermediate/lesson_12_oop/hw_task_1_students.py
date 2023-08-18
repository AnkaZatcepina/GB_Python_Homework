"""
Создайте класс студента.
    ○ Используя дескрипторы проверяйте ФИО на первую заглавную букву и
    наличие только букв.
    ○ Названия предметов должны загружаться из файла CSV при создании
    экземпляра. Другие предметы в экземпляре недопустимы.
    ○ Для каждого предмета можно хранить оценки (от 2 до 5) и результаты
    тестов (от 0 до 100).
    ○ Также экземпляр должен сообщать средний балл по тестам для каждого
    предмета и по оценкам всех предметов вместе взятых.
"""
import csv
class DescrName:   
    def __set_name__(self, owner, name):
        self.name = '_' + name
    def __get__(self, instance, owner):
        return getattr(instance, self.name)
    def __set__(self, instance, value):
        str(value).istitle()
        if str(value).istitle() and str(value).isalpha():
            setattr(instance, self.name, value)
        else:
            raise ValueError('ФИО должны начинаться на заглавную букву и состоять из букв')   

class Student:  
    _MIN_MARK = 2
    _MAX_MARK = 5
    _MIN_TEST = 0
    _MAX_TEST = 100

    name = DescrName()
    patr_name = DescrName()
    last_name = DescrName()

    def __init__(self, name: str, patr_name: str, last_name: str, subj_file: str = 'hw_task_1_subjects.csv'):
        self.name = name
        self.patr_name = patr_name
        self.last_name = last_name
        self._subjects = []
        with open(subj_file) as file:           
            for item in csv.reader(file, dialect='excel'):
                self._subjects += item
        self._marks = dict()     
        self._tests = dict()      

    def add_mark(self, subject:str, marks: [int]):
        for mark in marks:
            if not self._MIN_MARK <= mark <= self._MAX_MARK:
                raise ValueError(f'Оценка может быть от {self._MIN_MARK} до {self._MAX_MARK}')
            if subject in self._marks:
                self._marks[subject].append(mark)
            else:
                if not subject in self._subjects:
                    raise ValueError(f'Предмета {subject} не существует')
                self._marks[subject] = [mark]   
                
    def add_test(self, subject:str, tests: [int]):
        for test in tests:
            if not self._MIN_TEST <= test <= self._MAX_TEST:
                raise ValueError(f'Оценка может быть от {self._MIN_TEST} до {self._MAX_TEST}')
            if subject in self._tests:
                self._tests[subject].append(test)
            else:
                if not subject in self._subjects:
                    raise ValueError(f'Предмета {subject} не существует')
                self._tests[subject] = [test]   

    def get_average_mark(self) -> float:
        summa = 0
        count = 0
        for subject,marks in self._marks.items():
            for mark in marks:
                count += 1
                summa += mark
        return summa / count     

    def get_average_test(self, subject: str) -> float:
        summa = 0
        count = 0
        for mark in self._tests[subject]:
            count += 1
            summa += mark
        return summa / count           

    def __str__(self):
        result = f'Студент {self.name} {self.patr_name} {self.last_name}\n' \
                f'  Оценки: {self._marks}\n' \
                f'  Тесты: {self._tests}'  
        return result    

if __name__ == '__main__':
    student_1 = Student('Иван', 'Петрович', 'Иванов') 
    student_1.add_mark('Математика', [5,3])    
    student_1.add_mark('География', [4,5])      
    student_1.add_test('География', [0,98,100])    
    student_1.add_test('Русский язык', [70,80,80]) 
    print(student_1.get_average_mark())    
    print(student_1.get_average_test('География')) 

    print(student_1)

    