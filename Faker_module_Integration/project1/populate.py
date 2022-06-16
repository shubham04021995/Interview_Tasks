import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','project1.settings')
import django
django.setup()
import random
from app1.models import Employee
from faker import Faker

fake= Faker()

def populate(value):
    for i in range(value):
        eid=random.randint(1,200)
        ename= fake.name()
        esalary=random.randint(20000,80000)
        ecity =fake.city()

        obj = Employee.objects.get_or_create(
            eid=eid, ename=ename,esalary=esalary,ecity=ecity
        )


def main():
    no=int(input("How many records you want to add: "))
    populate(no)

if __name__=='__main__':
    main()    