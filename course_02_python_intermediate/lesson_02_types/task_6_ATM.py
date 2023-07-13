"""
    Напишите программу банкомат.
    ✔ Начальная сумма равна нулю
    ✔ Допустимые действия: пополнить, снять, выйти
    ✔ Сумма пополнения и снятия кратны 50 у.е.
    ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
    ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
    ✔ Нельзя снять больше, чем на счёте
    ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
    операцией, даже ошибочной
    ✔ Любое действие выводит сумму денег
"""
from enum import Enum

CURR = 'у.е.'

REST: int = 50
PRC_ADD_OPERATION_AMOUNT = 3
PRC_WITHDRAW = 1.5
PRC_ADD_ON_OPERATION = 3
PRC_WITHDRAW_VAL_MIN: int = 30
PRC_WITHDRAW_VAL_MAX: int = 600
PRC_100 = 100
WEALTH_SUM: int = 5_000_000
PRC_WEALTH_TAX = 10


class Command(Enum):
    TOP_UP      = "+"
    WITHDRAW    = "-"
    EXIT        = "exit"
summa: int = 0
operation_count: int = 0

# Вывод текщей суммы
def show_summa():
    print(f'Остаток на счёте: {summa} {CURR}')

# Проверка введённой суммы
def check_input_summa(summa: str) -> bool:
    if ( not summa.isdigit() ) or int(summa) % REST != 0:
        print(f'Некорректно введена сумма, введите число, кратное {REST}')
        return False  
    return True

# Пополнение процентов
def add_prc(summa: int) -> int:
    global operation_count
    operation_count += 1
    if operation_count % PRC_ADD_OPERATION_AMOUNT == 0: 
        show_summa()
        new_summa = int(summa * ( PRC_100 + PRC_ADD_ON_OPERATION ) / PRC_100)
        print(f'Вам начислено {PRC_ADD_ON_OPERATION}%')   
        return new_summa
    return summa  

# Снятие
def subtract(summa: int, value: int) -> int:
    withdraw_tax: int = int(value * PRC_WITHDRAW / PRC_100)
    if withdraw_tax < PRC_WITHDRAW_VAL_MIN: 
        withdraw_tax = PRC_WITHDRAW_VAL_MIN
    if withdraw_tax > PRC_WITHDRAW_VAL_MAX: 
        withdraw_tax = PRC_WITHDRAW_VAL_MAX
    value += withdraw_tax
    if value > summa:
        print(f'Невозможно снять сумму {value} с учётом процента снятия {withdraw_tax}')
    else:
        summa -= value
        summa = add_prc(summa)
    return summa   

# Вычитание налога на богатство
def subtract_wealth_tax(summa: int) -> int:
    print(f'Налог на богатство {PRC_WEALTH_TAX}%')    
    summa -= int(summa * PRC_WEALTH_TAX / PRC_100)
    return summa

while True:
    show_summa()
    command = input(f'Введите команду ("+" пополнить, "-" снять, "exit" выход): ')
    if summa > WEALTH_SUM:
        summa = subtract_wealth_tax(summa)
        show_summa() 
    match command:
        case Command.EXIT.value:
            break 
        case Command.TOP_UP.value:
            value = input(f"Введите сумму пополнения: ")
            if not check_input_summa(value):
                continue
            summa += int(value)
            summa = add_prc(summa)
        case Command.WITHDRAW.value:      
            value = input(f"Введите сумму снятия: ")      
            if not check_input_summa(value):
                continue
            summa = subtract(summa, int(value))
        case _:
            continue 
