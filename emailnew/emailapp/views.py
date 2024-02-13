from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponse

from django.core.mail import send_mail
from django.shortcuts import render, redirect

from django.conf import settings

from .forms import SubscribeForm


# Create your views here.



def subscribe(request):
    form = SubscribeForm()
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            subject = 'code band'
            message = 'Hi,How are you?'
            recipient = form.cleaned_data.get('email')
            send_mail(subject,message,settings.EMAIL_HOST_USER,[recipient],fail_silently=False )
            messages.success(request,'Success!')
            return redirect('subscribe')
    return render(request,"ureg.html")