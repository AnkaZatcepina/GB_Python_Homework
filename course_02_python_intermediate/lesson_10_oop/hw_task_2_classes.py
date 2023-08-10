"""
    Возьмите 1-3 любые задачи из прошлых семинаров (например сериализация данных), которые вы уже решали.
    Превратите функции в методы класса, а параметры в свойства. 
    Задачи должны решаться через вызов методов экземпляра.
"""
from random import randint

class QuadraticEquation:

    def __init__(self, a: float, b: float, c: float):
        self.a = a
        self.b = b
        self.c = c

    def solve(self) -> float | tuple[float,float] | tuple[complex,complex]: 
        d = self.b**2 - 4*self.a*self.c
        if d > 0:
            x_1 = (-self.b - d**0.5)/(2*self.a)
            x_2 = (-self.b + d**0.5)/(2*self.a)
            return(x_1,x_2)
        elif d == 0:
            x = -self.b/(2*self.a)  
            return(x)
        else:
            d = complex(d,0)
            x_1 = (-self.b - d**0.5)/(2*self.a)
            x_2 = (-self.b + d**0.5)/(2*self.a)           
            return(x_1,x_2)

class GuessNumb:

    def __init__(self, begin: int, end: int, attempts: int):
        self.begin = begin
        self.end = end
        self.attempts = attempts  

    def guess(self) -> bool:
        numb: int = 0
        rand_numb: int = randint(self.begin, self.end)
        for _ in range(self.attempts):
            numb = int(input(f'Введите число от {self.begin} до {self.end}: '))
            if numb == rand_numb:
                print('Верно!')
                return True
            elif numb < rand_numb:
                print('Больше') 
            elif numb > rand_numb:
                print('Меньше') 
        print('Количество попыток закончилось!')       
        return False            

if __name__ == '__main__':
    quadratic_equation =  QuadraticEquation(-2,5,1)
    print(quadratic_equation.solve())  

    guess_numb = GuessNumb(1, 10, 3)
    guess_numb.guess()