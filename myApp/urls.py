from django.contrib import admin
from django.urls import path
from myApp import views



urlpatterns = [
    path("", views.index, name='myApp'),
    path("about", views.about, name='myApp'),
    path("services", views.services, name='myApp'),
    path("contact", views.contact, name='myApp')
]
