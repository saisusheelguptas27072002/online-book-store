from django.contrib import admin
from django.urls import path
from insem import views
urlpatterns = [
    path('', views.login, name="login"),
    path('home', views.home, name="home"),
    path('add', views.addBook, name="addBook")
]
