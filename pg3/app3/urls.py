from django.urls import path
from .views import lists
urlpatterns=[
    path('',lists,name="lists")
]