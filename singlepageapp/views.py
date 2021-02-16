from django.http.response import HttpResponse
from django.shortcuts import render,HttpResponseRedirect
from .models import Inquiry

from django.core.mail import send_mail
# Create your views here.
def index(request):
    return render(request,'index.html')

def submit(request):
    name=request.POST['name']
    mobile=request.POST['mobile']
    email=request.POST['email']
    inquiry=request.POST['inquiry']
    pay=request.POST['pay']
    need=request.POST['need']
    data=Inquiry(name=name,mobile=mobile,email=email,inquiry=inquiry,pay=pay,need=need)
    data.save()
    subject = 'Free Consultation Inquiry'
    message = 'name: '+name+'\nmobile: '+mobile+'\nemail: '+email+'\nInquiry: '+inquiry+'\nReady to Pay: '+pay+'\nRequirements: '+need
    send_mail(subject, 
            message,'dhavalmaniyar123@gmail.com', ['dhavalmaniyar123@gmail.com'], fail_silently = False)
    return render(request,'index.html',{'message':"Thank You, we will contact you soon"})