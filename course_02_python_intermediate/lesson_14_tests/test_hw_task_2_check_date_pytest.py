"""
Возьмите 1-3 задачи из тех, что были на прошлых
семинарах или в домашних заданиях.
📌 Напишите к ним тесты.    
"""
from hw_task_2_check_date_doctest import check_date
import pytest

def test_correct():
    assert check_date('01.01.2021'), 'correct date test failed'

def test_ranges():
    assert not check_date('32.14.2021'),'incorrect check of range: 1<=day<=31, 1<=month<=12, 1<=year<=9999'

def test_days_in_month_amount():
    assert not check_date('31.04.2021'),'incorrect check days in month'

def test_days_in_february():
    assert not check_date('30.02.2020'),'incorrect check days in February'  

def test_days_in_february_leap_year():  
    assert not check_date('29.02.2001'),'incorrect check of leap year'
    
if __name__ == '__main__':
    pytest.main(['-vv'])