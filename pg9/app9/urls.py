from django.urls import path
from .views import enrollform,enrolment
urlpatterns=[
    path('',enrollform,name="enrolmentform"),
    path('enroll/',enrolment,name="enroll")

]