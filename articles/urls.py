from django.urls import path
from . import views

# class import 

# from .views import Articles

urlpatterns = [
    path('', views.home, name='home'),
    path('create', views.create, name='create'),
    path('articles', views.articles, name='articles'),
    path('articles/<str:pk>', views.article_view, name='article_view'),
]