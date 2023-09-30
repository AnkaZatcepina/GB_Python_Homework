from django.shortcuts import render
from django.http import HttpResponse 
from django.shortcuts import get_object_or_404 
import random
from . import models
  
def random_coin(request): 
    answer = ['Орёл', 'Решка']
    result = random.choice(answer)
    result_m = models.Coin(result=result)
    result_m.save()
    return HttpResponse(result_m) 

def get_last_coins(request): 
    n = request.GET.get('n', '5')
    return HttpResponse(models.Coin.statistic(int(n)).items())   

def get_authors(request): 
    authors = models.Author.objects.all()
    #result = '\n'.join(str(author) for author in authors)
    return HttpResponse(authors)     

def get_articles(request): 
    articles = models.Article.objects.all()

    context = {"articles": articles}
    return render(request, "lesson_02_app/articles.html", context)
    #return HttpResponse(articles)   

def get_article(request, article_id: int): 
    article = get_object_or_404(models.Article, pk=article_id)
    article.show_count += 1
    article.save()
    comments = models.Comment.objects.filter(article_id=article_id).order_by('-modificated_date')
    context = {
        'article': article,
        'comments': comments
    }

    return render(request, "lesson_02_app/article_detail.html", context)    

#/lesson2/articles/by_author?name=Name2
def get_articles_by_author(request): 
    author_id = None
    name = request.GET.get('name')
    author = models.Author.objects.filter(name=name).first()
    if author:
        author_id = author.pk 

    articles = models.Article.objects.filter(author=author)
    #articles = models.Article.objects.filter(author_id=author_id)
    #articles = models.Article.objects.filter(author__pk=author_id)

    return HttpResponse(articles)          

def get_comments(request): 
    comments = models.Comment.objects.all()
    return HttpResponse(comments)    