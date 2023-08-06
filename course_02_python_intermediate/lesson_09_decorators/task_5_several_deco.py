"""
    📌 Объедините функции из прошлых задач.
    📌 Функцию угадайку задекорируйте:
    ○ декораторами для сохранения параметров,
    ○ декоратором контроля значений и
    ○ декоратором для многократного запуска.
    📌 Выберите верный порядок декораторов.
"""

from task_2_decorator import deco as validate
from task_3_deco_json import add_params_to_json
from task_4_param_deco import param_deco as launch_qty


@launch_qty(3)
@validate
#Если логирование сделть позже, то логироваться будет wrapper, а не сама функция
@add_params_to_json
def guess_numb(numb:int, attempts:int):
    for i in range(1, attempts+1):
        print(f'Номер попытки {i}')
        answer = int(input(f'Введите число от 1 до 100:'))
        if answer == numb:
            print('Верно!')
            break
        elif answer > numb:
            print('Меньше')
        else:
            print('Больше')

if __name__ == '__main__':
    guess_numb(15, 2)