from django.urls import path
from .views import list_cource,reg_student,student_detail,reg_cource
urlpatterns=[
    path('',list_cource,name="list-cource"),
    path('register_student/',reg_student,name="reg_student"),
    path('register_cource/',reg_cource,name="reg_cource"),
    path('student_detail/<int:course_id>/',student_detail,name="student_detail"),

]