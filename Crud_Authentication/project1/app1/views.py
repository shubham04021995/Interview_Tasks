
from django.shortcuts import redirect, render
from .models import Laptop
from .forms import LaptopForm


def lapview(request):
    form = LaptopForm()
    template_name="app1/laptopform.html"
    context={'form':form}

    if request.method=="POST":
        form=LaptopForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show.urls')
    return render (request,template_name,context)

def showlaptop(request):
    data=Laptop.objects.all()
    template_name="app1/showlaptop.html"
    context={'data':data}
    return render(request,template_name,context)    

def updatelaptop(request,laptop_id):
    obj=Laptop.objects.get(laptop_id=laptop_id)
    form=LaptopForm(instance=obj)
    template_name="app1/laptopform.html"
    context={'form':form}

    if request.method =="POST":
        form=LaptopForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return redirect('show.urls')
    return render(request,template_name,context)  


def deletelaptop(request,laptop_id):
    obj=Laptop.objects.get(laptop_id=laptop_id)
    template_name="app1/confirmation.html"
    context={'obj':obj}

    if request.method=="POST":
        obj.delete()
        return redirect('show.urls')
    return render(request,template_name,context)              


# Create your views here.
