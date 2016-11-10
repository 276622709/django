# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
import os
import commands
def index(request):
    return render(request,'index.html')
def command(request):
    a=os.popen('ifconfig')
    return HttpResponse(a.read().replace("\n","<br>"))
def command1(request):
    b=os.popen('uptime')
    return HttpResponse(b.read())
def get(request):
    b=request.GET['haha']
    print(b)
    c=commands.getoutput(b)
    print(c)
    return HttpResponse(c.replace("\n","<br>"))
