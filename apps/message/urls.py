__author__ = 'Administrator'
from django.urls import path
from . import views
urlpatterns = [
    path('index', views.index, name='message'),
]