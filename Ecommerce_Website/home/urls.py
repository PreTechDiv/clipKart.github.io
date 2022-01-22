from django import views
from django.contrib import admin
from django.urls import include, path
from home import views

urlpatterns = [
    path('index/', views.index , name='index'),
    path('about/', views.about , name='about'),
    path('search/', views.search , name='search')
    
]