"""
📌 Создайте новое приложение. Подключите его к проекту. В
приложении должно быть три простых представления,
возвращающих HTTP ответ:
📌 Орёл или решка
📌 Значение одной из шести граней игрального кубика
📌 Случайное число от 0 до 100
📌 Пропишите маршруты

📌 Добавьте логирование в проект.
📌 Настройте возможность вывода в файл и в терминал.
📌 Устраните возможные ошибки.

Задание №3
📌 Маршруты могут принимать целое число - количество
бросков.
📌 Представления создают список с результатами бросков и
передают его в контекст шаблона.
📌 Необходимо создать универсальный шаблон для вывода
результатов любого из трёх представлений.
"""
import logging
import random
from django.shortcuts import render
from django.http import HttpResponse 

logger = logging.getLogger(__name__)

def random_coin(request, count: int): 
    answer = ['Орёл', 'Решка']
    result = []
    for _ in range(count):
        result.append(random.choice(answer))
    logger.info(result)
    content = {
        'items': result,
        'count': count
    }
    return render(request, "lesson_01_task_2_app/random.html", content) 
    
def random_dice(request, count: int):
    result = []
    for _ in range(count):
        result.append(random.randint(1, 7))
    logger.info(result) 
    content = {
        'items': result,
        'count': count
    }
    return render(request, "lesson_01_task_2_app/random.html", content)

def random_hundred(request, count: int): 
    result = []
    for _ in range(count):
        result.append(random.randint(0, 101))
    logger.info(result)
    content = {
        'items': result,
        'count': count
    }
    return render(request, "lesson_01_task_2_app/random.html", content)    
