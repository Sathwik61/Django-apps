from django.urls import path
from .views import date_time
urlpatterns=[
    path('time/',date_time,name="date_time"),
]