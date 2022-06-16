from django.contrib import admin
from .models import Laptop


class LaptopAdmin(admin.ModelAdmin):
    list_display=['laptop_id','name','brand','rom','rom','HDD']

admin.site.register(Laptop,LaptopAdmin)    

# Register your models here.
