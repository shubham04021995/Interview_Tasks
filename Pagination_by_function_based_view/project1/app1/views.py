from django.core.paginator import Paginator,EmptyPage
from django.shortcuts import redirect, render
from .forms import EmployeeForm
from .models import Employee


def empview(request):
    form=EmployeeForm()
    template_name='app1/employeeform.html'
    context={'form':form}


    if request.method=="POST":
        form=EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("show.urls")
    return render(request,template_name,context)

def showemp(request):
    data=Employee.objects.all()
    
    paginator= Paginator(data,5) 
    try:
        if request.GET.get('page'):
            data=paginator.page(request.GET.get('page'))
        else:
            data=paginator.page(1)

    except EmptyPage:
        data=paginator.page(paginator.num_pages)

    template_name='app1/showemployee.html' 

    context={'data':data}
    return render(request,template_name,context)   

def updateview(request,eid):
    obj=Employee.objects.get(eid=eid)
    form=EmployeeForm(instance=obj)
    template_name='app1/employeeform.html'
    context={'form':form}

    if request.method=="POST":
        form=EmployeeForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return redirect("show.urls")
    return render(request,template_name,context)

def  deleteview(request,eid):
    obj=Employee.objects.get(eid=eid)
    template_name='app1/confirmation.html'
    context={'obj':obj}  
    


    if request.method=="POST":
            obj.delete()
            return redirect("show.urls")

    return render(request,template_name,context)    




# Create your views here.
