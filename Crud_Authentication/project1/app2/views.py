from email import message
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.conf import settings
from django.core.mail import send_mail
from random import randint
from django.contrib.auth.models import User
from django.views import View
from .forms import RegistartionForm


def generate_otp():
    return randint(1000,9999)

class Register(View):
    form=RegistartionForm
    template_name="app2/register.html"

    def get (self,request):
        form=self.form()
        context={'form':form}
        return render(request,self.template_name,context)


    def post (self,request):
        form=self.form(request.POST)       

        if form.is_valid():
            email=request.POST.get('email')
            name=request.POST.get('username')

            subject ="Registartion Details"
            message=f'Hello {name}, {email} You Are Successfully Register'
            from_email=settings.EMAIL_HOST_USER
            recipient_list =[email,]

            status= send_mail(subject,message,from_email,recipient_list)
            print(status)

            if status:
                form.save()
                return redirect('login.urls')
        context={'form':form}
        return render(request,self.template_name,context)        


class Login(View):
    template_name="app2/loginpage.html"

    def get(self,request):
        context={}
        return render(request,self.template_name,context)


    def post(self,request):
        un = request.POST.get('u')
        pw =request.POST.get('p')

        user=authenticate(username=un,password=pw)

        if user is not None:
            #login(request,user)
            otp=generate_otp()
            mail=user.email
            subject="Registration Details",
            message =f'Hello Your otp is{otp} \n Thanks for visit.'
            from_email=settings.EMAIL_HOST_USER
            recipient_list =[mail,]
            send_mail(subject,message,from_email,recipient_list)

            resp=render(request,'app2/OTP.html',context={'user':user})
            #resp=redirect('otp.urls')
            
            resp.set_cookie("otp",otp,max_age=30)
            return resp

        context={}
        return render(request,self.template_name,context)    


class Logout(View):
    def get (self,request):
        logout(request)
        return redirect('login.urls') 

class VerifyOTPview(View):
    template_name='app2/OTP.html'

    def get(self,request):
        return render(request=request,template_name=self.template_name)

    def post(self,request):
        otp1=request.POST.get('otp')
        resp=request.COOKIES.get('otp')
        id=request.POST.get('user')
        user=User.objects.get(pk=id)

        if  otp1==resp and user:
            print(otp1,resp)
            login(request,user)
            return redirect('show.urls')
        return render(request,self.template_name)                           

# Create your views here.
