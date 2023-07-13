"""
    ✔ Создайте вручную список с повторяющимися целыми числами.
    ✔ Сформируйте список с порядковыми номерами
    нечётных элементов исходного списка.
    ✔ Нумерация начинается с единицы.
"""

my_list = [1,3,1,3,6,7,8,5,8,1,1]

new_list = []
for i in range(len(my_list)):
    if my_list[i] % 2 == 1:
       new_list.append(i+1) 
print(new_list)

new_list_2 = []
for i, value in enumerate(my_list, start=1):
    if value % 2 == 1:
       new_list_2.append(i) 
print(new_list_2)
