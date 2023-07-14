"""
    ✔ Создайте вручную список с повторяющимися элементами.
    ✔ Удалите из него все элементы, которые встречаются дважды.
"""
from collections import defaultdict

my_list

my_list_2 = [1,3,1,3,6,7,8,5,8,1,1]
amount_dict_2 = defaultdict(int)
for item in my_list_2:
    amount_dict_2[item] += 1

for key, value in amount_dict_2.items():
    if value == DUPLICATES:
        for _ in range(DUPLICATES):
            my_list_2.remove(key)  

print(my_list_2)  
