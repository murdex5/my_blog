from multiprocessing import context
import re
from urllib.request import Request
from django.shortcuts import render
from django.http import HttpResponse

from .models import *

# Create your views here.

def home(request):
    return HttpResponse('home')


def create(request):
    return HttpResponse('create')


def articles(request):
    
    articles_list = Article.objects.all()
    
    context = {
        'articles': articles_list,
    }
    return render(request, 'articles.html', context)


def article_view(request, pk):
    
    article_id = Article.objects.get(id=pk)
    article = article_id.order_set.all()
    
    title = article.title()
    author = article.author()
    body = article.body()
    
    context = {
        'id':pk,
        # 'title': title,
        # 'author': author,
        # 'body': body,
        'article': article
    }
    return render(request, 'article_view.html', context)