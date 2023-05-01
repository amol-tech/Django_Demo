from faker import Faker
import random
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE','proj_demo.settings')
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
django.setup()
from app_demo.models import Department,Employee
import datetime


fake_gen = Faker()
dict_desig = {'Sales':['Area Manager','Salesman','Officer'],
             'Production':['Manager','Production Head','Engineer','Labour'],
             'Account':['Manager','Officer','Clerk'],
             'Purchase':['Manager','Officer','Clerk']}

def get_basic_fact(desig):
    if 'Manager' in desig:
        return 100
    elif desig == 'Production Head':
        return 50
    elif desig in ['Officer','Engineer']:
        return 20
    else:
        return 10

def add_department(id, name, location, start_range, end_range):
    dept = Department.objects.get_or_create(id=id, name=name, location=location)[0]
    dept.save()
    designations = dict_desig.get(name)

    for i in range(start_range, end_range):
        emp_id = 'E' + ('00' if i <= 9 else ('0' if i <= 99 else '')) + str(i)
        desig = random.choice(designations)
        basic_fact = get_basic_fact(desig)

        emp = Employee.objects.get_or_create(id=emp_id,
                                             name=fake_gen.name(),
                                             designation=desig,
                                             joining_date=fake_gen.date_between(datetime.date(2016, 1, 1),
                                                                                datetime.date(2021, 12, 30)),
                                             basic=fake_gen.pydecimal(left_digits=5, right_digits=0,
                                                                      positive=True) * basic_fact,
                                             allowence=fake_gen.pydecimal(left_digits=3, right_digits=0,
                                                                          positive=True) * basic_fact,
                                             address=fake_gen.street_address(),
                                             city=fake_gen.city(),
                                             contact_no=fake_gen.phone_number(),
                                             department=dept)[0]
        emp.save()
    print('Successfully generated data for department : '+name)