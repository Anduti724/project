"""myapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from re import template

from django.shortcuts import redirect
from coreapp import views
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as ask

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('restourant/',views.restourant_home,name='restourant_home'),
  
    path('restourant/sign_in/', ask.LoginView.as_view(template_name='restourant/sign_in.html'),name='restourant_sign_in'),
    path('restourant/sign_out/', ask.LogoutView.as_view(next_page='/'),name='restourant_sign_out'),
    path('restourant/sign_up/',views.restourant_sign_up,name='restourant_sign_up'),



]
