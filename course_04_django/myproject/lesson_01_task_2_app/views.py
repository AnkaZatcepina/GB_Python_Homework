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
"""
import logging
import random
from django.shortcuts import render
from django.http import HttpResponse 

logger = logging.getLogger(__name__)

def random_coin(request): 
    answer = ['Орёл', 'Решка']
    result = random.choice(answer)
    logger.info(result)
    return HttpResponse(result) 
    
def random_dice(request):
    result = random.randint(1, 7)
    logger.info(result) 
    return HttpResponse(result)

def random_hundred(request): 
    result = random.randint(0, 101)
    logger.info(result)
    return HttpResponse(result)    
