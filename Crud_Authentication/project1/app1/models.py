from django.db import models

class Laptop(models.Model):
    laptop_id=models.IntegerField(primary_key=True)
    name =  models.CharField(max_length=30)
    brand = models.CharField(max_length=40)
    ram = models.CharField(max_length=10)
    rom = models.CharField(max_length=10)
    HDD = models.CharField(max_length=10)
    mail = models.EmailField(null=True)

    def _str__(self):
        return f"{self.laptop_id}--{self.name}--{self.brand}--{self.ram}--{self.rom}--{self.HDD}"


# Create your models here.
