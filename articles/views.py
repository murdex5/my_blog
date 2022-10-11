from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers

from .models import Article
# Create your views here.



def home(request):
    articles = serializers.serialize( "python", Article.objects.all() )
    context = {
        'articles': articles,
    }
    
    return render(request, 'home.html', context=context)


def article(request, pk):
    pk = Article.objects.get(id=pk)
    name = Article.title()
    body = Article.body()
    author = Article.author()
    
    context = {
        'name': name,
        'body': body,
        'author': author,
    }
    return render(request, 'article-view.html', context=context)