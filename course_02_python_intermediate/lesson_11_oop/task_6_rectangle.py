"""
    📌 Доработайте прошлую задачу.
    📌 Добавьте сравнение прямоугольников по площади
    📌 Должны работать все шесть операций сравнения
"""
from lesson_10_oop.task_2_rectangle import Rectangle

class RectanglePro(Rectangle):
    def __add__(self, other):
        summa:int = self.get_perimeter()+other.get_perimeter()
        length = self.length + other.length
        width = summa//2 - length
        return RectanglePro(length,width)
    def __sub__(self,other):
        if self.get_perimeter() < other.get_perimeter():
            self, other = other,self
        diff:int = self.get_perimeter()-other.get_perimeter()
        length = abs(self.length - other.length)
        width = diff//2 - length
        return RectanglePro(length,width)

    def __eq__(self,other):
        return self.get_area() == other.get_area()

    def __gt__(self,other):
        return self.get_area() > other.get_area()

    def __le__(self,other):
        return self.get_area() <= other.get_area()        

if __name__ == '__main__':
    rectangle_1 = RectanglePro(3,1)
    rectangle_2 = RectanglePro(2,4)
    rectangle_3 = RectanglePro(4,2)
    print(rectangle_1 == rectangle_2)
    print(rectangle_2 == rectangle_3)
    print(rectangle_1 > rectangle_3)
    print(rectangle_1 <= rectangle_3)
    print(rectangle_2 < rectangle_3)
    print(rectangle_2 <= rectangle_3)