"""
📌 Создайте класс с базовым исключением и дочерние классы-
исключения:
    ○ ошибка уровня,
    ○ ошибка доступа.
"""
from task_4_access_level import User

class MyException(Exception):
    pass

class LevelException(MyException):
    def __init__(self, user: User, access_level: int):
        self.user = user 
        self.access_level = access_level
    def __str__(self):
        return f'Нельзя добавить пользователя с уровнем {self.access_level}.' \
                f'Вы вошли как {self.user.name} с уровнем {self.user.access_level}. '

class AccessException(MyException):
    def __init__(self, name: str, user_id: int):
        self.name = name 
        self.user_id = user_id 
    def __str__(self):
        return f'Отказано в доступе, пользователь id={self.user_id}, name={self.name} не найден.'