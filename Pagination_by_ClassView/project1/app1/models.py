from django.db import models


class Laptop(models.Model):
    laptop_id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=20)
    brand=models.CharField(max_length=20)
    ram=models.CharField(max_length=20)
    rom=models.CharField(max_length=20)
    HDD=models.CharField(max_length=20)
    image= models.ImageField(blank=True, upload_to='blog_images')
    description=models.FileField(blank=True,upload_to='blog_pdf')

    def __str__(self):
        return f"{self.laptop_id}--{self.name}"

# Create your models here.
