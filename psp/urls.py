"""django_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from django.conf.urls import url
from psp import views
urlpatterns = [
    url(r'^index$', views.index),
    url(r'^books$', views.show_books),
    url(r'^creat$', views.creat),
    url(r'^delete/(\d+)$', views.delete),
    url(r'^books/(\w+)$', views.show_book_detial),
    url('^login$', views.login),
    url('^login_check$', views.login_check),
    url(r'^ajax_test$', views.ajax_test),
    url(r'ajax_handle$', views.ajax_handel)
]
