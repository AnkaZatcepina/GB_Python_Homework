#Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
def countEven(intList):
    sum = 0
    for index, value in enumerate(intList):
        if ( index % 2 == 1 ):
            sum += value 
    return sum

list = [2, 3, 5, 9, 3]
print(countEven(list))    