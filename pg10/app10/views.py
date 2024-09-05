from django.shortcuts import render
from django.http import JsonResponse
from .models import Students

def search(r):
    if r.headers.get('x-requested-with') == 'XMLHttpRequest':
        student_name = r.GET.get('sname')
        if student_name:
            try:
                student = Students.objects.get(name__iexact=student_name)
                courses = student.courses.all()
                course_list = [course.name for course in courses]
                return JsonResponse({"data": course_list,"status":200})
            except Students.DoesNotExist:
                return JsonResponse({"data": "Student not found"})
    else:
        return render(r, 'index.html')

def home(r):
    return render(r, 'index.html')
