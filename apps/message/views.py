from django.shortcuts import render,redirect,HttpResponse
from . import models
# Create your views here.
def index(request):
     if request.method=='POST':
        name=request.POST.get('username',None)#一般采用这种
        print(name)
        email=request.POST.get('email',None)
        address=request.POST.get('address',None)
        message=request.POST.get('message',None)
        res = models.UserMessage.objects.create(name=name,email=email,address=address,message=message)
        if res:
            return  redirect("/message/index")
        else:
            return  HttpResponse("添加失败")
     return  render(request,'message/from.html')
