from django.shortcuts import render
from django.http import HttpResponse

from .models import Article
# Create your views here.



def home(request):
    article = Article.objects.first()
    context = {'article': article}
    
    return render(request, 'home.html', context=context)