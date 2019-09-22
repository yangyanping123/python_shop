from django.shortcuts import render
from django.shortcuts import HttpResponse,render,redirect
# Create your views here.
def index(request):
     return  HttpResponse("hello blog1")