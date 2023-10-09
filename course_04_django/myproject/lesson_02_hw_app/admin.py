from django.contrib import admin

"""
Задание №2
    📌 Подключите к админ панели созданные вами в рамках прошлых семинаров модели в приложении магазин
"""
from . import models
# Register your models here.
admin.site.register(models.Client)
admin.site.register(models.Product)
admin.site.register(models.Order)
admin.site.register(models.OrderProduct)
