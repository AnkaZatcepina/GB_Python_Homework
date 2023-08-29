"""
Возьмите любые 1-3 задачи из прошлых домашних заданий.
Добавьте к ним логирование ошибок и полезной
информации. Также реализуйте возможность запуска из
командной строки с передачей параметров.
"""
import logging
import argparse

logging.basicConfig(filename='hw_task_1.log', encoding='utf-8', level=logging.INFO)
logger = logging.getLogger(__name__)

def parse():
    parser = argparse.ArgumentParser(prog='check_date', 
                                    description='Проверка даты на корректный ввод', 
                                    epilog='Пример запуска: python3.10 hw_task_1_check_date.py -d "30.01.2010"')
    parser.add_argument('-d', '--date', help='Дата в формате dd.mm.yyyy')
    args = parser.parse_args()
    return check_date(args.date)

def if_leap(year: int) -> bool:
    return not(year % 4 != 0 or year % 100 == 0 and year % 400 != 0)

def check_date(str_date: str) -> bool:
    day, month, year = map(int, str_date.split('.'))
    if not( 1 <= day <= 31 and 1 <= month <= 12 and 1 <= year <= 9999 ):
        logger.error(f'{str_date} - некорректная дата')
        return False
    if month in (4,6,9,11) and day > 30:
        logger.error(f'{str_date} - неверное количество дней {day} в месяце {month}')
        return False
    if month == 2 and day > 29:
        logger.error(f'{str_date} - неверное количество дней {day} в феврале')
        return False
    if month == 2 and not if_leap(year) and day > 28:
        logger.error(f'{str_date} - год {year} не високосный, в нём не может быть {day} дней')
        return False

    logger.info(f'{str_date} - корректная дата')            
    return True       

if __name__ == '__main__':
    parse()