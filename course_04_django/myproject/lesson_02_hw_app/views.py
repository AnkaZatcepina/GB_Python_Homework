"""
Создайте три модели Django: клиент, товар и заказ.

Клиент может иметь несколько заказов. Заказ может содержать несколько товаров. Товар может входить в несколько заказов.

Поля модели «Клиент»:
    — имя клиента
    — электронная почта клиента
    — номер телефона клиента
    — адрес клиента
    — дата регистрации клиента

Поля модели «Товар»:
    — название товара
    — описание товара
    — цена товара
    — количество товара
    — дата добавления товара

Поля модели «Заказ»:
    — связь с моделью «Клиент», указывает на клиента, сделавшего заказ
    — связь с моделью «Товар», указывает на товары, входящие в заказ
    — общая сумма заказа
    — дата оформления заказа

Допишите несколько функций CRUD для работы с моделями по желанию. 
"""
from django.shortcuts import render
from django.http import HttpResponse 
from . import models
import decimal

def get_clients(request):
    clients = models.Client.objects.all()
    return HttpResponse(clients)

def get_products(request):
    products = models.Product.objects.all()
    return HttpResponse(products)

#lesson2/orders_by_client?client_id=3
def get_orders_by_client(request):
    client_id = request.GET.get('client_id')
    orders = models.Order.objects.filter(client__pk=client_id)
    return HttpResponse(orders)          

def create_order(request):
    client_id = request.GET.get('client_id')
    order = models.Order(client_id=client_id)
    order.save()
    return HttpResponse(order) 

#lesson2/add_product_to_order/?order_id=16&product_id=5
def add_product_to_order(request):
    order_id = request.GET.get('order_id')
    product_id = request.GET.get('product_id')
    order = models.Order.objects.filter(pk=order_id).first()
    product = models.Product.objects.filter(pk=product_id).first()         
    order.products.add(product)
    order.save()
    return HttpResponse(order)        

def update_product_price(request, product_id: int, price: int):
    product = models.Product.objects.filter(pk=product_id).first()
    if product:
        product.price = price
        product.save()
        return HttpResponse('Цена товара изменена')
    else:
        return HttpResponse('Товар не найден')

def delete_order(request, order_id: int):
    order = models.Order.objects.filter(pk=order_id).first()
    if order:
        order.delete()
        return HttpResponse('Заказ удален')
    else:
        return HttpResponse('Заказ не найден')        