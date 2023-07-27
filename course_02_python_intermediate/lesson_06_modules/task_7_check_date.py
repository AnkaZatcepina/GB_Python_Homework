"""
    Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
    Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
    Для простоты договоримся, что год может быть в диапазоне [1, 9999]. 
    Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь. 
    Проверку года на високосность вынести в отдельную защищённую функцию.
"""

def if_leap(year: int) -> bool:
    return not(year % 4 != 0 or year % 100 == 0 and year % 400 != 0)

def check_date(str_date: str) -> bool:
    day, month, year = map(int, str_date.split('.'))
    if not( 1 <= day <= 31 and 1 <= month <= 12 and 1 <= year <= 9999 ):
        return False
    if month in (4,6,9,11) and day > 30:
        return False
    if month == 2 and day > 29:
        return False
    if month == 2 and not if_leap(year) and day > 28:
        return False

    return True       

if __name__ == '__main__':
    print(check_date('29.02.2000')) 
    print(check_date('29.02.2001')) 
    print(check_date('31.04.2001'))  
    print(check_date('31.44.2001'))