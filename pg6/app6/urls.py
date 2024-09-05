from django.urls import path
from .views import projectlist,reg_project,reg_students,details

urlpatterns=[
    path('',projectlist,name="projectlist"),
    path('reg_project/',reg_project,name="reg_project"),
    path('reg_students/',reg_students,name="reg_students"),
    path('details/<int:p_id>/',details,name="details"),

]