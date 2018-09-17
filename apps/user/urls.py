from django.conf.urls import include, url
from django.contrib import admin
from user import views

urlpatterns = [
    url(r'^register$',views.register),
    url(r'rpost',views.rpost)  
]