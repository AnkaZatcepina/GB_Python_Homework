"""
    ✔ Вручную создайте список с целыми числами, которые
    повторяются. Получите новый список, который содержит
    уникальные (без повтора) элементы исходного списка.
    ✔ *Подготовьте два решения, короткое и длинное, которое
    не использует другие коллекции помимо списков.
"""

my_list = [1,3,1,3,6,7,8,5,8]
new_list = []
for item in my_list:
    if item not in new_list:
        new_list.append(item)
print(new_list)    

new_list_2 = list(set(my_list))
print(new_list_2)  