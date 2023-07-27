"""
    Добавьте в пакет, созданный на семинаре шахматный модуль. 
    Внутри него напишите код, решающий задачу о 8 ферзях. 
    Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.
    Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга. 
    Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей. 
    Если ферзи не бьют друг друга верните истину, а если бьют - ложь.
    Напишите функцию в шахматный модуль. 
    Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше. 
    Проверяйте различные случайные  варианты и выведите 4 успешных расстановки.
"""

__all__ = ['check_8_queens','random_check_8_queens']

from random import randint

QUEENS = 8
ROWS = 8
SOLUTIONS = 4

def check_8_queens(queens: [(int)]) -> bool:
    for i in range(QUEENS):
        for j in range(i+1,QUEENS):
            i_coord = queens[i]
            j_coord = queens[j]
            if i_coord[0]==j_coord[0] or i_coord[1]==j_coord[1]:
                return False
            if abs(i_coord[0]-j_coord[0]) == abs(i_coord[1]-j_coord[1]):
                return False    
    return True

def random_check_8_queens():
    solution = 0
    while solution < SOLUTIONS:
        queens_count = 0        
        queens = [None] * QUEENS
        while queens_count < QUEENS:
            x = randint(1,ROWS)
            y = randint(1,ROWS)
            if (x,y) not in queens:
                queens[queens_count]=(x,y)
                queens_count += 1
        if check_8_queens(queens):
            print(f'Решение № {solution}: {queens}') 
            solution += 1 
    return

if __name__ == '__main__':
    print(check_8_queens([(1,2),(2,3),(4,5),(6,7),(8,1),(1,2),(2,3),(7,7)]))
    print(check_8_queens([(1,4),(2,1),(3,5),(4,8),(5,2),(6,7),(7,3),(8,6)]))
    random_check_8_queens()