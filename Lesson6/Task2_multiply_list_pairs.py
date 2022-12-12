#Предложить улучшения кода для уже решённых задач:
#С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension
#Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
import math

def multiply_list_pairs(int_list):
    length = len(int_list)
    left_list = int_list[:int(math.ceil(length / 2))]
    right_list = int_list[length // 2::]
    right_list.reverse()
    mult_list = list(map(lambda l, r: l * r, left_list, right_list))
    return mult_list

list1 = [2, 3, 4, 5, 6]
print(multiply_list_pairs(list1)) 
list2 = [2, 3, 5, 6]
print(multiply_list_pairs(list2)) 