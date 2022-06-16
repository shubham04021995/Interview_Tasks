from django.shortcuts import render,redirect
from .models import Customer
from .forms import CustomerForm
from .utils import render_to_pdf,render_to_pdf1
from django.views import View

class AddView(View):
    template_name='app1/addcus.html'
    form=CustomerForm
    def get(self,request):
        form=self.form()
        context={'form':form}
        return render(request,self.template_name,context)

    def post(self,request):
        form=self.form(request.POST)
        context={'form':form}

        if form.is_valid():
            form.save()
            return redirect('showurl')
        return render(request,self.template_name,context)


class Showdata(View):
    template_name='app1/showcus.html'
    def get(self,request):
        obj=Customer.objects.all().order_by("id")
        context={'obj':obj}
        return render(request,self.template_name,context)


class ShowoneCus(View):
    template_name='app1/singlepdf.html'
    def get(self,request,id):
        obj=Customer.objects.get(id=id)
        return render_to_pdf1(
        self.template_name,
        {
            "obj":obj,
        },    
        )

class ShowCus(View):
    template_name='app1/showpdf.html'
    def get(self,request):
        obj=Customer.objects.all().order_by("id")
        return render_to_pdf(
        self.template_name,
        {
            "obj":obj,
        },
        )        



# Create your views here.
