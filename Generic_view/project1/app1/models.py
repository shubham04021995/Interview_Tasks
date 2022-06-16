from django.db import models


class Laptop(models.Model):
    laptop_id = models.IntegerField(primary_key=True)
    name= models.CharField(max_length=20)
    brand = models.CharField(max_length=30)
    ram = models.CharField(max_length=20)
    rom =models.CharField(max_length=20)
    HDD = models.CharField(max_length=40)

    def __str__(self):
        return f'{self.laptop_id}--{self.name}--{self.brand}--{self.ram}--{self.rom}--{self.HDD}'
# Create your models here.
