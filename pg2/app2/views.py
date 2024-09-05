from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from datetime import timedelta

def time(req):
    currenttime=datetime.now()
    delta=timedelta(hours=+4)
    newtime=delta+currenttime
    beforetime=currenttime-delta
    html=f'<html><div>Current time :{currenttime}</div><br/><div>Time 4 hours ahead:{newtime}</div><br/><div> Time 4 Hours before:{beforetime}</div></html>'
    return HttpResponse(html)