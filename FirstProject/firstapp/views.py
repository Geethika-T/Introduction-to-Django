from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def project(request):
    return HttpResponse("Hello World")

def home(request):
    return render(request,'Home.html')