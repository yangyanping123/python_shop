from django.shortcuts import render
from django.shortcuts import HttpResponse,render,redirect
# Create your views here.

def index(request):
     return  reversed("home:index")

def home(request):
    pass

def product(request):
    pass
def market(request):
    pass