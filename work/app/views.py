from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render

from .forms import CustomUserCreationForm, bookForm
from .models import Book


# Create your views here.


def home(request):
    return render(request,'home.html')
def home1(request):
    return HttpResponse('SUCCESSFULL')

def adminhome(request):
    return  render(request,'adminhome.html')

def employeehome(request):
    return render(request,'employeehome.html')

def managerhome(request):
    return render(request,'manager.html')

def employeesignup(request):
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if (form.is_valid()):
            f = form.save(commit=False)
            f.is_employee = True
            f.save()
            return  home(request)
    return render(request,'employeesignup.html',{'form':form})

def managersignup(request):
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.is_manager = True
            f.save()
            return home(request)
    return render(request,'managersignup.html',{'form':form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        print(user)
        if user and user.is_superuser == True:
            login(request,user)
            return  adminhome(request)
        elif user and user.is_employee == True:
            login(request,user)
            return employeehome(request)
        elif user and user.is_manager == True:
            login(request,user)
            return managerhome(request)
        else:
            return HttpResponse("Invalid Login credentials...")

    return render(request,'login.html')



def upload1(request):
    form = bookForm
    if request.method == 'POST':
        form=bookForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return home1(request)

    return render(request,'upload1.html',{'form':form})
def upload(request):
    k=Book.objects.all()
    return render(request,'upload.html',{'s':k})
def delete_book(request,pk):
    b=Book.objects.get(pk=pk)
    b.delete()
    return upload(request)
def view_book(request,pk):
    b=Book.objects.get(pk=pk)
    context ={
        'instance':b,
        'title':'View Book'
    }
    return render(request,'book.html',context)

def edit_book(request,pk):
    view=Book.objects.get(pk=pk)
    form=bookForm(instance=view)
    if request.method == "POST":
        form = bookForm(request.POST, request.FILES, instance=view)
        if form.is_valid():
            form.save(commit=True)
            return home(request)
        else:
            print("ERROR FORM INVALID")
    return render(request, 'upload1.html', {'form': form})

def user_logout(request):
    logout(request)
    return home(request)

