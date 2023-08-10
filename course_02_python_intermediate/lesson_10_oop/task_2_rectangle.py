"""
    📌 Создайте класс прямоугольник.
    📌 Класс должен принимать длину и ширину при создании
    экземпляра.
    📌 У класса должно быть два метода, возвращающие периметр
    и площадь.
    📌 Если при создании экземпляра передаётся только одна
    сторона, считаем что у нас квадрат.
"""

class Rectangle:
    def __init__(self, length: int, width: int = None):
        self.length = length
        self.width = width if width != None else length

    def get_perimeter(self)->int:
        return 2 * ( self.length + self.width )

    def get_area(self)->int:       
        return self.length * self.width  

if __name__ == '__main__':
    rectangle = Rectangle(3,1)
    print(rectangle.get_perimeter())      
    print(rectangle.get_area())  