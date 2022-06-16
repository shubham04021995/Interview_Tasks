
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm



def registerview(request):
    form=UserCreationForm()
    template_name='AUTH_APP/register.html'
    context={'form':form}

    if request.method=="POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login.urls")
    return render(request,template_name,context)


def loginview(request):
    template_name='AUTH_APP/loginpage.html'
    context={}


    if request.method=="POST":
        un=request.POST.get("u")
        pw=request.POST.get("p")

        user=authenticate(username=un, password=pw)

        if user is not None:
            login(request,user)
            
            return redirect("show.urls")
    return render(request,template_name,context)        
# Create your views here.
