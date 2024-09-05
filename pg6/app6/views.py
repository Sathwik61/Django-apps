from django.shortcuts import render
from .models import Students, Project
from .form import StduentForm, ProjectForm

def projectlist(r):
    projects=Project.objects.all()
    return render(r,'home.html',{'projects':projects})

def reg_project(r):
    form=ProjectForm()
    if r.method=="POST":
        form=ProjectForm(r.POST)
        if form.is_valid():
            form.save()
            return render(r,'success.html',{"title":"Project"})
    else:
        form=ProjectForm()
    return render(r,'register_project.html',{'form':form})

def reg_students(r):
    form=StduentForm()
    if r.method=="POST":
        form=StduentForm(r.POST)
        if form.is_valid():
            form.save()
            return render(r,'success.html',{"title":"Student"})
    else:
        form=StduentForm()
    return render(r,'register_student.html',{'form':form})

def details(r,p_id):
    project=Project.objects.get(id=p_id)
    students=project.projectname.all()
    # print(students)
    return render(r,'details.html',{"details":students,"project":project})
