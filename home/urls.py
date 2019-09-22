__author__ = 'Administrator'
from django.urls import path,re_path
from . import views
urlpatterns = [
     path('',views.index), #执行blog下面view index的方法
]