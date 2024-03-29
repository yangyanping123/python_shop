"""shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from django.views.static import serve
from shop.settings import MEDIA_ROOT
import xadmin
urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path('home/', include('home.urls')),
    path('message/', include('message.urls')),
      #配置上传文件的访问处理函数
   #url(r'^media/(?P<path>.*)$',  serve, {"document_root":MEDIA_ROOT}),
]
