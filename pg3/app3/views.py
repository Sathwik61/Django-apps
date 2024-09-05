from django.shortcuts import render

# Create your views here.
def lists(req):
    fruits=['apple','banana','pinapple','mango']
    students=['Dheeraj','David','Dravid','Dolly']
    context={
        "students":students,
        "fruits":fruits
    }
    return render(req,'index.html',context)