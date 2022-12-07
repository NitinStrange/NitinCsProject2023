"""CsProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
'''from django.contrib import admin'''
from django.urls import path
from django.contrib import admin
from login.views import home,signup,login,pg2_1,pg2_2,pg2_3,pg2_4,pg3

urlpatterns = [
    path('admin', admin.site.urls, name='admin'),
    path('signup', signup, name='signup'),
    path('signin', login, name='signin'),
    path('', home, name='home'),
    path('crickat', pg2_1, name='crickat'),
    path('basketball', pg2_2, name='basketball'),
    path('football', pg2_3, name='football'),
    path('volleyball', pg2_4, name='volleyball'),
    path('XXX', pg3, name='xxx')
]
