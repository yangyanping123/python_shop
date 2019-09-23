__author__ = 'Administrator'
from django.urls import path
from . import views
urlpatterns = [
     path('',views.home,name='index'), #执行blog下面view index的方法
     path('home',views.index,name='home'), #执行blog下面view index的方法
     path('product',views.product,name='product'), #执行blog下面view index的方法
     path('market',views.market,name='market'), #执行blog下面view index的方法
]