from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return HttpResponse("Hello world")
def hello(request):
    return render(request,'myhome.html')