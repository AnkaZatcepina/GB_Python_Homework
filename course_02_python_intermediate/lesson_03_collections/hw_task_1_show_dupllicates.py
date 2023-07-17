"""
    Дан список повторяющихся элементов. 
    Вернуть список с дублирующимися элементами. 
    В результирующем списке не должно быть дубликатов.
"""

my_list = [1,3,1,3,6,7,8,5,8,1,1]
amount_dict = {}

for item in my_list:
    key = amount_dict.setdefault(item,0) 
    amount_dict[item] += 1

for key, value in amount_dict.items():
    if value == 1:
        my_list.remove(key)  

my_list = list(set(my_list))
print(my_list)  
