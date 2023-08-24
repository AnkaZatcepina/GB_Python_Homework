"""
Возьмите 1-3 задачи из тех, что были на прошлых
семинарах или в домашних заданиях.
📌 Напишите к ним тесты.    
"""
import math

class Circle:
    def __init__(self, radius: int):
        self.radius = radius

    def get_length(self)->float:
        """
        >>> t.get_length()
        18.84955592153876
        """
        return 2 * math.pi * self.radius

    def get_area(self)->float:  
        """
        >>> t.get_area()
        28.274333882308138
        """     
        return  math.pi * self.radius ** 2      

if __name__ == '__main__':
    import doctest
    doctest.testmod(extraglobs={'t': Circle(3)}, verbose=True)
   
    