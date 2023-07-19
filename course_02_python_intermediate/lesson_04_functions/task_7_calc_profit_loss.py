"""
    ✔ Функция получает на вход словарь с названием компании в качестве ключа
    и списком с доходами и расходами (3-10 чисел) в качестве значения.
    ✔ Вычислите итоговую прибыль или убыток каждой компании. Если все компании
    прибыльные, верните истину, а если хотя бы одна убыточная — ложь.
"""

def is_all_profit(companies: {str: [int]}) -> bool:

#    for companie in companies.values():
#        if sum(companie) < 0:
#            return False
#    return True   
    return all(map(lambda x: sum(x) > 0, companies.values()))


companies = {
    'samsung': [100,-300,1200,500],
    'google': [357,677,-350,-500,100],
    'apple': [-900,-300,447,300,-1000],
}
print(is_all_profit(companies))