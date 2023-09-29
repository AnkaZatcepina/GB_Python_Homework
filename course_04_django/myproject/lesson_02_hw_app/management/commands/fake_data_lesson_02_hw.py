from django.core.management.base import BaseCommand
from ... import models
import random

class Command(BaseCommand):
    help = "Generate fake clients, products and orders"
    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='amount')
    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, count + 1):
            client = models.Client(
                name=f'Client{i}', 
                email=f'mail{i}@mail.ru',
                phone=f'+7(908)00{i}',
                address=f'Street, Home {i}',
            )
            client.save()
            product = models.Product(
                name=f'Product{i}', 
                description=f'Descr{i}',
                price=100*i,
                quantity=10+i,
            )
            product.save()
        clients = models.Client.objects.all()
        products = models.Product.objects.all()

        for _ in range(count):
            random_client = models.Client.objects.order_by('?')[0]
            order = models.Order(
                client=random_client,                
            )
            order.save()
            for j in range(3):
                random_product = models.Product.objects.order_by('?')[0]            
                order.products.add(random_product)
            order.save()
        