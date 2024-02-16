from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render

from .forms import CustomUserCreationForm


# Create your views here.
def home(request):
    return render(request,'home.html')


def adminhome(request):
    return render(request,'adminhome.html')


def employeehome(request):
    return render(request,'employeehome.html')


def ceohome(request):
    return render(request,'ceohome.html')



def employeesignup(request):
    form =CustomUserCreationForm()
    if request.method =="POST":
        form = CustomUserCreationForm(request.POST)
        if (form.is_valid()):
            f = form.save(commit=False)
            f.is_employee = True
            f.save()
            return home(request)
    return render(request,'employeesignup.html',{'form':form})


def ceosignup(request):
    form = CustomUserCreationForm()
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.is_ceo = True
            f.save()
            return home(request)
    return render(request, 'ceosignup.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        print(user)
        if user and user.is_superuser == True:
            login(request,user)
            return adminhome(request)
        elif user and user.is_employee == True:
            login(request,user)
            return employeehome(request)
        elif user and user.is_ceo == True:
            login(request,user)
            return ceohome(request)
        else:
            return HttpResponse("Invalid login details.....")

    return render(request, 'login.html')


def user_logout(request):
    logout(request)
    return home(request)
