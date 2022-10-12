import re
from urllib.request import Request
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse('home')


def catalog(request):
    return HttpResponse('catalog')


def create(request):
    return HttpResponse('create')

def article_view(request):
    return HttpResponse('article-view')