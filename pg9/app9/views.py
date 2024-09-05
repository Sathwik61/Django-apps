from django.shortcuts import render
from .models import Student
from .form import StudentForm
from django.http import JsonResponse

def enrollform(r):
    form=StudentForm()
    return render(r,'index.html',{'form':form})
def enrolment(r):
    if r.method=='POST' and r.headers.get('x-requested-with')=='XMLHttpRequest':
        form=StudentForm(r.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({"msg":"Form saved successfully"})
        else:
            err=form.errors.as_json()
            return JsonResponse({"msg":err})
        


