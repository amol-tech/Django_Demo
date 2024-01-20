from faker import Faker
import random
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE','proj_demo.settings')
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
django.setup()
from app_demo.models import Department,Employee,Customer,Product,Sales,SalesItem
import datetime
import pandas as pd


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

def create_customers(start_index,end_index):
    fake_gen = Faker()
    
    for i in range(start_index,end_index):
        cust_id = 'C' + ('00' if i <= 9 else ('0' if i <= 99 else '')) + str(i)
        c_limit = random.choice([10,15,20,30,12,8])
        cust = Customer.objects.get_or_create(id=cust_id,
                                              name=fake_gen.name(),
                                              credit_limit=c_limit,
                                              address = fake_gen.address().replace('\n',''),
                                              landmark=fake_gen.street_address(),
                                              city=fake_gen.city(),
                                              state=fake_gen.state())[0]
        cust.save()
    print('Customers created successfully')    

def create_employees(id, name, location, start_range, end_range):
    dept = Department.objects.get_or_create(id=id, name=name, location=location)[0]
    dept.save()
    designations = dict_desig.get(name)

    for i in range(start_range, end_range):
        emp_id = 'E' + ('00' if i <= 9 else ('0' if i <= 99 else '')) + str(i)
        desig = random.choice(designations)
        basic_fact = get_basic_fact(desig)
        
        try:
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
        except:
            print('Failed to create employee')
    print('Successfully generated data for department : '+name)

def create_products():
    df_prod = pd.read_csv('product.csv')
    list_dict_prod = df_prod.to_dict('records')
    for d_prod in list_dict_prod:
        prod = Product.objects.get_or_create(id=d_prod['id'],
                                                  name=d_prod['name'],
                                                  manufacturer=d_prod['manufacturer'],
                                                  cost_rate=d_prod['cost_rate'])[0]
        prod.save()
    print('Products created successfully')
    
def create_sales(start_index,end_index,start_date,end_date):
    
    customers = Customer.objects.all()
    products = Product.objects.all()
    fake_gen = Faker()
    
    for i in range(start_index, end_index):
        cust = random.choice(customers)
        gross_amt = 0
        # Sales
        sales = Sales.objects.get_or_create(id=i,
                                            date=fake_gen.date_between(start_date,end_date),
                                            customer = cust,
                                            gross_amount = 0,
                                            disc_rate = random.choice([5,10,15,20]),
                                            disc_amount = 0,
                                            net_amount = 0)[0]
        sales.save()
        
        # Sales Items
        for i in range(1,random.randint(2,8)):
            prod = random.choice(products)
            qty = random.randint(1,6)
            rate = prod.cost_rate + (100 * random.randint(5,20))
            amt = rate * qty
            salesitem = SalesItem.objects.get_or_create(sales = sales,
                                            product = prod,
                                            rate = rate,
                                            qty = qty,
                                            amount = amt)[0]
            salesitem.save()
            
            gross_amt = gross_amt + amt
        
        # Update Sales
        disc = gross_amt * sales.disc_rate / 100
        sales.gross_amount = gross_amt
        sales.disc_amount = disc
        sales.net_amount = gross_amt - disc
        sales.save()
    print('Sales created successfully in a range of ',start_index,'-',end_index)
    

#create_employees('D01','Sales','Mumbai',1,60)
#create_employees('D02','Account','Bangalore',61,100)
#create_employees('D03','Production','Pune',101,140)
#create_employees('D04','Purchase','Hydrabad',141,160)
#create_customers(1,21)
#create_products()
create_sales(1,100,datetime.date(2021, 1, 1),datetime.date(2021, 12,31))
create_sales(101,200,datetime.date(2022, 1, 1),datetime.date(2022, 12,31))
create_sales(201,300,datetime.date(2023, 1, 1),datetime.date(2023, 12,31))