#Предложить улучшения кода для уже решённых задач:
#С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension
#Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
def sum_even(int_list):
    return sum(int_list[x] for x in range(1, len(int_list), 2))

list = [2, 3, 5, 9, 3]
print(sum_even(list))    