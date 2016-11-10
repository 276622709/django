# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from .forms import AddForm
import os
def index(request):
    return render(request,'index.html')
def command(request):
    a=os.popen('ifconfig')
    return HttpResponse(a.read().replace("\n","<br>"))
def command1(request):
    b=os.popen('uptime')
    return HttpResponse(b.read())
