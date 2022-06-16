from django.db import models

class Customer(models.Model):
    cid = models.IntegerField()
    name = models.CharField(max_length=50)
    mobile = models.IntegerField()
    city = models.CharField(max_length=50)
    bill = models.FloatField()

    def __str__(self):
        return f"{self.cid}--{self.name}"
    

# Create your models here.
