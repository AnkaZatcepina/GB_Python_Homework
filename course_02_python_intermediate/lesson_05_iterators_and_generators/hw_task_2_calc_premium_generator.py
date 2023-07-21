"""
    Напишите однострочный генератор словаря, который принимает
    на вход три списка одинаковой длины: имена str, ставка int,
    премия str с указанием процентов вида «10.25%». В результате
    получаем словарь с именем в качестве ключа и суммой
    премии в качестве значения. Сумма рассчитывается
    как ставка умноженная на процент премии
"""

import decimal

def calc_premium(names: [str], salaries: [int], proсs: [str]) -> {str: int}:
    return {name: salary * decimal.Decimal(proс[:-1]) / 100 \
            for name, salary, proс in zip(names, salaries, proсs)}       
    return 

names = ['Вася', 'Петя', 'Дима']   
salaries = [1000, 2000, 1000]  
proсs = ['10.25%', '11%', '12.25%'] 

print(*calc_premium(names, salaries, proсs).items())