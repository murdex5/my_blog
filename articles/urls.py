from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='index'),
    path('articles/<int:pk>', views.article, name='articles'),
]