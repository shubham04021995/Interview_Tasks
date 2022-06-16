from django.shortcuts import render,redirect
from .models import Employee
from .forms import EmployeeForm





def showemp(request):
    data=Employee.objects.all()
    template_name='app1/showemp.html'
    context={'data':data}
    return render(request,template_name,context)
# Create your views here.
