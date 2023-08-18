"""
📌 Доработайте класс прямоугольник из прошлых семинаров.
📌 Добавьте возможность изменять длину и ширину
прямоугольника и встройте контроль недопустимых значений
(отрицательных).
📌 Используйте декораторы свойств.
"""
class Rectangle:
    """
    Rectangle Class to add, subtract and compare rectangles
    """    
    def __init__(self, length: int, width: int = None):
        self._length = length
        self._width = width if width != None else length

    def get_perimeter(self)->int:
        return 2 * ( self._length + self._width )

    def get_area(self)->int:       
        return self._length * self._width  

    def __add__(self, other):
        """
        Add rectangles
        """
        summa:int = self.get_perimeter()+other.get_perimeter()
        length = self._length + other._length
        width = summa//2 - length
        return RectanglePro(length,width)
    def __sub__(self,other):
        """
        Subtract rectangles
        """
        if self.get_perimeter() < other.get_perimeter():
            self, other = other,self
        diff:int = self.get_perimeter()-other.get_perimeter()
        length = 1
        width = diff//2 - length
        return RectanglePro(length,width)

    def __eq__(self,other):
        return self.get_area() == other.get_area()

    def __gt__(self,other):
        return self.get_area() > other.get_area()

    def __le__(self,other):
        return self.get_area() <= other.get_area()  

    def __str__(self):
        return f'Length = {self._length}, Width = {self._width}'

    def __repr__(self):
        return f"RectanglePro({self._length},{self._width})" 

    @property
    def length(self):     
        return self._length
    @property
    def width(self):     
        return self._width

    @length.setter
    def length(self, value):
        if value >= 0:
            self._length = value
        else:
            raise ValueError('Значения меньше или равные нулю недопустимы')     

    @width.setter
    def width(self, value):
        if value >= 0:
            self._width = value 
        else:
            raise ValueError('Значения меньше или равные нулю недопустимы')            

if __name__ == '__main__':
    rectangle = Rectangle(3,1)
    rectangle.length = 5
    print(rectangle.length)
    rectangle.length = -5
    print(rectangle.length)