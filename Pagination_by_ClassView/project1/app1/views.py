from email.mime import image
from django.shortcuts import render,redirect
from .models import Laptop
from .forms import LaptopForm
from django.views import View
from django.core.paginator import Paginator,EmptyPage


class AddLap(View):
    template_name='app1/addlap.html'
    form=LaptopForm
    
    def get(self,request):
        form=self.form()
        context={'form':form}
        return render(request,self.template_name,context)

    def post(self,request):
        form=self.form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect("show.urls")  
        context={'form':form}
        return render(request,self.template_name,context)  

class Showlap(View):
    template_name='app1/showlap.html'    

    def get(self,request):
        obj=Laptop.objects.all()
        paginator=Paginator(obj,5)
        try:
            if request.GET.get('page'):
                obj=paginator.page(request.GET.get('page'))

            else:
                obj =paginator.page(1)

        except EmptyPage:
            obj=paginator.page(paginator.num_pages)
        
        context={'obj':obj}
        return render(request,self.template_name,context)         


class Updatelap(View):
    template_name='app1/addlap.html'
    form=LaptopForm

    def get(self,request,pk):
        data=Laptop.objects.get(pk=pk)
        form=self.form(instance=data)
        context={'form':form}
        return render(request,self.template_name,context)

    def post(self,request,pk):
        data=Laptop.objects.get(pk=pk)
        form=self.form(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect("show.urls")
        context={'form':form}
        return render(request,self.template_name,context)

class Deletelap(View):
    template_name='app1/confirmation.html'

    def get(self,request,pk):
        obje= Laptop.objects.get(pk=pk)
        context={'obje':obje}
        return render(request,self.template_name,context)

    def post(self,request,pk):
        obje=Laptop.objects.get(pk=pk)
        obje.delete()
        context={'obje':obje}
        return redirect("show.urls") 
        #return render(request,self.template_name,context)   




# Create your views here.
