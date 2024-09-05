from django.urls import path
from .views import StudentDetailView,StudentView
urlpatterns=[
    path('students/',StudentView.as_view(),name="list"),
    path('students/<int:pk>/',StudentDetailView.as_view(),name="detailed"),
]