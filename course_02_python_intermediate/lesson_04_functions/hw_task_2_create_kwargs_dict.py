"""
    Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, 
    где ключ — значение переданного аргумента, а значение — имя аргумента. 
    Если ключ не хешируем, используйте его строковое представление.
"""

def create_kwargs_dict(**kwargs)-> {}:
    result = {}
    for key,value in kwargs.items():
        value_formatted = value
        try:
            hash(value_formatted)
        except:
           value_formatted = str(value)     
        result[value_formatted] = key
    return result 

print(create_kwargs_dict(my_ind=1, my_str='Test', my_tuple=(1,2), my_list=[1,2]))       