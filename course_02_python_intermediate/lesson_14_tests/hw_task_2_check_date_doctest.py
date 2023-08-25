"""
Возьмите 1-3 задачи из тех, что были на прошлых
семинарах или в домашних заданиях.
📌 Напишите к ним тесты.    
"""

def if_leap(year: int) -> bool:
    return not(year % 4 != 0 or year % 100 == 0 and year % 400 != 0)

def check_date(str_date: str) -> bool:
    """
    Checks if date in format DD.MM.YYYY is correct

    >>> check_date('01.01.2000')
    True
    >>> check_date('29.02.2001')
    False
    """
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
    import doctest
    doctest.testmod(verbose=True)