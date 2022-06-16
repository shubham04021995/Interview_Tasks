from django.db import models


class Employee(models.Model):
    eid=models.IntegerField(primary_key=True)
    ename=models.CharField(max_length=20)
    esalary=models.FloatField()
    ecity=models.CharField(max_length=40)


    def __str__(self):
        return f"{self.eid}--{self.ename}"   

# Create your models here.
