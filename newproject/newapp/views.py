from django.http import HttpResponse
from django.shortcuts import render

from.models import product


# Create your views here.
def index(request):
    return HttpResponse("HELLO")
def ind(request):
    items={
        'item':product.objects.all()
    }
    return render(request,'index.html',items)