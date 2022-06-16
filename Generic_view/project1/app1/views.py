
from django.urls import reverse_lazy

from .models import Laptop
from django.views.generic import UpdateView,DeleteView,ListView,CreateView,DetailView

class LaptopCreate(CreateView):
    model=Laptop
    fields="__all__"

    #template_name='app1/laptop_form.html'
    success_url=reverse_lazy('show.urls')

class LaptopView(ListView):
    model=Laptop
    template_name='app1/showlaptop.html'
    #context_object_name='data'   


class LaptopDetails(DetailView):
    model=Laptop
    template_name='app1/laptopdetails.html'  


class updateView(UpdateView):
    model=Laptop
    fields="__all__"
    #template_name="app1/showlaptop.html"
    success_url=reverse_lazy("show.urls")       
  
class deleteView(DeleteView):
    model=Laptop
    template_name="app1/confirmation.html"    
    success_url=reverse_lazy("show.urls")

# Create your views here.
