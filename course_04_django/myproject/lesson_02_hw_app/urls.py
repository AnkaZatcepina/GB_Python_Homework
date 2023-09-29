from django.urls import path, include
from . import views 


urlpatterns = [ 
    path('clients/', views.get_clients, name='clients'),
    path('products/', views.get_products, name='products'),
    path('orders_by_client/', views.get_orders_by_client, name='orders_by_client'), 
    path('create_order/', views.create_order, name='create_order'),
    path('add_product_to_order/', views.add_product_to_order, name='add_product_to_order'),
    path('update_product_price/<int:product_id>/<int:price>', views.update_product_price, name='update_product_price'),
    path('delete_order/<int:order_id>', views.delete_order, name='delete_order'),
    
]