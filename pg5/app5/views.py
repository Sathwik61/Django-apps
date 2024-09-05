from django.shortcuts import render,redirect, get_object_or_404
from .foms import StudentForm,CourceForm
from .models import Students,Cources
def list_cource(r):
    cources=Cources.objects.all()
    return render(r,'courcelist.html',context={'cources':cources})

def student_detail(r,course_id):
    course = Cources.objects.get(id=course_id)
    student=course.students.all()
    return render(r,'stu_list.html',{'student':student})
def reg_cource(r):
    if r.method=='POST':
        form=CourceForm(r.POST)
        if form.is_valid():
            form.save()
            return render(r,'success.html')
    else:
        form=CourceForm()
    return render(r, 'registerstudent.html', {'form': form})   

def reg_student(r):
    if r.method=='POST':
        form=StudentForm(r.POST)
        if form.is_valid():
            form.save()
            return render(r,'success.html')
    else:
        form=StudentForm()
    return render(r, 'registerstudent.html', {'form': form})   