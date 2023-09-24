from django.urls import path 
from . import views 

urlpatterns = [ 
    path('coin/', views.random_coin, name='coin'), 
    path('dice/', views.random_dice, name='dice'), 
    path('hundred/', views.random_hundred, name='hundred'), 
]