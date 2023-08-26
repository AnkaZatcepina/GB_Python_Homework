"""
    📌 Дорабатываем задачу 4.
    📌 Добавьте возможность запуска из командной строки.
    📌 При этом значение любого параметра можно опустить. В
    этом случае берётся первый в месяце день недели, текущий
    день недели и/или текущий месяц.
    📌 *Научите функцию распознавать не только текстовое
    названия дня недели и месяца, но и числовые,
    т.е не мая, а 5.
"""

import logging
from datetime import datetime
import argparse

logging.basicConfig(filename='task_4,log',encoding='utf-8',level=logging.ERROR)
logger = logging.getLogger(__name__)

WEEKDAYS = ('пон', 'вто', 'сре', 'чет', 'пят', 'суб', 'вос')
MONTHS = ('янв', 'фев', 'мар', 'апр', 'мая', 'июн', 'июл', 'авг', 'сен', 'окт', 'ноя', 'дек')

def parse():
    parser = argparse.ArgumentParser(prog='text_2_date', 
                                    description='Получение даты из строки', 
                                    epilog='Пример: text_2_date("3-я среда мая")')
    parser.add_argument('-n', '--numb', default=1, help='Какой по счёту день недели')
    parser.add_argument('-w', '--weekday', default=datetime.now().weekday, help='Название дня недели')
    parser.add_argument('-m', '--month', default=datetime.now().month, help='Название месяца в родительном падеже')
    args = parser.parse_args()
    return text_2_date(f'{args.numb} {args.weekday} {args.month}')

def text_2_date(text: str)->datetime:

    try:
        numb_text, weekday_text, month_text = text.split()
    except ValueError as e:
        logger.error(f'Невозможно корректно разбить строку "{text}". {e}')
        return None
    try:        
        numb = int(numb_text[0]) 
    except ValueError as e:
        logger.error(f'Невозможно достать порядковый номер "{numb}". {e}')
        return None
    try:  
        weekday = WEEKDAYS.index(weekday_text[:3])
    except ValueError as e:
        logger.error(f'Не существет дня недели "{weekday_text}". {e}')
        return None
    try:  
        month = MONTHS.index(month_text[:3]) + 1
    except ValueError as e:
        logger.error(f'Не существет месяца "{month_text}". {e}')
        return None
    
    i = 0
    year = datetime.now().year
    result = None
    for day in range(1,32):
        date = datetime(year=year, month=month, day=day)
        if date.weekday() == weekday:
            i += 1
            if i == numb:
                return date

    logger.error(f'Не существет такого дня "{text}"')
    return None

if __name__ == '__main__':
    print(parse())  

#пример запуска в коиандной строке 
# python3.10 task_5_argparse.py --help
# python3.10 task_5_argparse.py -n 1-й -w четверг -m ноября    