"""
    📌 Дорабатываем класс прямоугольник из прошлого семинара.
    📌 Добавьте возможность сложения и вычитания.
    📌 При этом должен создаваться новый экземпляр
    прямоугольника.
    📌 Складываем и вычитаем периметры, а не длинну и ширину.
    📌 При вычитании не допускайте отрицательных значений.
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
        length = 1
        width = diff//2 - length
        return RectanglePro(length,width)

if __name__ == '__main__':
    rectangle_1 = RectanglePro(4,2)
    rectangle_2 = RectanglePro(1,3)
    rectangle_3 = rectangle_1 + rectangle_2
    print(rectangle_3.length, rectangle_3.width)
    rectangle_4 = rectangle_1 - rectangle_2
    print(rectangle_4.length, rectangle_4.width)