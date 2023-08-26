"""
    📌 Функция получает на вход текст вида: “1-й четверг ноября”, “3-я среда мая” и т.п.
    📌 Преобразуйте его в дату в текущем году.
    📌 Логируйте ошибки, если текст не соответсвует формату.
"""
import logging
from datetime import datetime

logging.basicConfig(filename='task_4,log',encoding='utf-8',level=logging.ERROR)
logger = logging.getLogger(__name__)

WEEKDAYS = ('пон', 'вто', 'сре', 'чет', 'пят', 'суб', 'вос')
MONTHS = ('янв', 'фев', 'мар', 'апр', 'мая', 'июн', 'июл', 'авг', 'сен', 'окт', 'ноя', 'дек')

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
    print(text_2_date('1-й четверг ноября'))   
    print(text_2_date('3-я среда мая'))  
    print(text_2_date('среда мая'))  