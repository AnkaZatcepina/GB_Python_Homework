"""
    ✔ Создайте вручную кортеж содержащий элементы разных типов.
    ✔ Получите из него словарь списков, где:
    ключ — тип элемента,
    значение — список элементов данного типа.
"""

my_tuple = (1,'two',-2.2,True,None,0.0004, False, 0, 'text')

my_dict = {}
for item in my_tuple:
    if type(item) in my_dict:
        my_dict[type(item)].append(item)
    else:  
        my_dict[type(item)] = [item] 
print(my_dict)

my_dict_2 = {}
for item in my_tuple:
    key = my_dict_2.setdefault(type(item),[]) 
    key.append(item)
print(my_dict_2)
