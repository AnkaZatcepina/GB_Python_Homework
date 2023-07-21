"""
    ✔ Продолжаем развивать задачу 2.
    ✔ Возьмите словарь, который вы получили.
    Сохраните его итераторатор.
    ✔ Далее выведите первые 5 пар ключ-значение,
    обращаясь к итератору, а не к словарю.
"""
MAX = 5

my_str = 'abacaaddefg'
my_dict = {key: ord(key) for key in my_str }
my_iterator = iter(my_dict.items())
for _ in range(MAX):
    print(next(my_iterator))
