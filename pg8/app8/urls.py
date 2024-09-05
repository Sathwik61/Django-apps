from django.urls import path
from .views import booktocsv,booktopdf,home
urlpatterns=[
    path('csv/',booktocsv,name="csv"),
    path('pdf/',booktopdf,name="pdf"),
    path('',home,name="home"),
]