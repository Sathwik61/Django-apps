from django.urls import path
from .views import time 
urlpatterns=[
    path('',time,name="time"),
]