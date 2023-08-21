"""
    📌 Создайте функцию аналог get для словаря.
    📌 Помимо самого словаря функция принимает ключ и
    значение по умолчанию.
    📌 При обращении к несуществующему ключу функция должна
    возвращать дефолтное значение.
    📌 Реализуйте работу через обработку исключений.
"""

def my_get(my_dict: dict, key: str, default: int | float = None) -> int | float | None:
    result = default
    try:
        result = my_dict[key]
    except KeyError as e:
        pass
    return result

if __name__ == '__main__':
    my_dict = {'a': 56, 'b': 3.4}
    print(my_get(my_dict, 'a'))    
    print(my_get(my_dict, 'c'))      
    print(my_get(my_dict, 'c', '1'))
