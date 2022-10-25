from wsgiref.handlers import read_environ
from django.shortcuts import render

# Create your views here.

def index(request,*args, **kwargs):
    return render(request,'frontend/index.html')