"""
    Возьмите 1-3 задачи из тех, что были на прошлых
    семинарах или в домашних заданиях. Напишите к ним
    классы исключения с выводом подробной информации.
    Поднимайте исключения внутри основного кода. Например
    нельзя создавать прямоугольник со сторонами
    отрицательной длины.
"""

class NonPositiveNumberException(Exception):
    def __init__(self, value: int):
        self.value = value 
    def __str__(self):
        return f'Нельзя использовать число меньше или равное нулю "{self.value}"'

class Rectangle:
    def __init__(self, length: float, width: float | None = None):
        try:
            self.length = float(length)
        except ValueError as e:
            print(f'Длину "{length}" не удалось привести к числу')
            raise
        try:
            self.width = float(width) if width != None else self.length
        except ValueError as e:
            print(f'Ширину "{width}" не удалось привести к числу')  
            raise  
        if self.length <= 0:
            raise NonPositiveNumberException(self.length)   
        if self.width <= 0:
            raise NonPositiveNumberException(self.width)

    def get_perimeter(self)->float:
        return 2 * ( self.length + self.width )

    def get_area(self)->float:       
        return self.length * self.width  

if __name__ == '__main__':
    #rectangle_1 = Rectangle(3,1)
    #rectangle_2 = Rectangle('test',1)
    rectangle_3 = Rectangle(-3,0)
