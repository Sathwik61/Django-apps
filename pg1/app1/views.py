from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
def date_time(req):
    time=datetime.now()
    
    return HttpResponse(f'<html><div>{time}</div></html>')
