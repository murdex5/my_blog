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