from django.shortcuts import render

def home(req):
    return render(req,'home.html')
def contact(req):
    return render(req,'contact.html')
def about(req):
    return render(req,'about.html')