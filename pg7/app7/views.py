from django.shortcuts import render
from .models import Student
# Create your views here.
from django.views.generic import ListView,DetailView

class StudentView(ListView):
    model=Student
    template_name='slist.html'
    context_object_name='students'

class StudentDetailView(DetailView):
    model=Student
    template_name='sdetail.html'
    context_object_name='students'