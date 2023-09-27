from django.urls import path, include
from . import views 

articles_patterns = [
    path('/', views.get_articles, name='articles'),
    path('by_author/', views.get_articles_by_author, name='articles_by_author'),
]

urlpatterns = [ 
    #path('', views.index, name='index'), 
    path('random_coin/', views.random_coin, name='random_coin'), 
    path('get_last_coins/', views.get_last_coins, name='get_last_coins'), 
    path('authors/', views.get_authors, name='authors'),
    path('articles/', include(articles_patterns)),
]