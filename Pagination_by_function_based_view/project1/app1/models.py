from django.db import models

class Employee(models.Model):
    eid=models.IntegerField(primary_key=True)
    ename=models.CharField(max_length=50)
    ecity=models.CharField(max_length=20,null=True)
    esalary=models.FloatField(null=True)
    edept=models.CharField(max_length=10,null=True)


    def __str__(self):
        return f"{self.eid}--{self.ename}"
# Create your models here.
