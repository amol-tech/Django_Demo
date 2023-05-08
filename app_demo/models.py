from django.db import models

# Create your models here.
class Department(models.Model):
    id = models.CharField(max_length=3,primary_key=True,db_column='dept_id')
    name = models.CharField(max_length=50,db_column='dname',unique=True)
    location = models.CharField(max_length=50,db_column='loc')

    class Meta:
        db_table = 'dept'

    def __str__(self):
        return self.name

class Employee(models.Model):
    id = models.CharField(max_length=4,primary_key=True,db_column='emp_id')
    name = models.CharField(max_length=255,db_column='ename',unique=True)
    designation = models.CharField(max_length=40,db_column='desig')
    joining_date = models.DateField(db_column='doj')
    basic = models.DecimalField(max_digits=12,decimal_places=2,db_column='basic')
    allowence = models.DecimalField(max_digits=12,decimal_places=2,db_column='allowence')
    address = models.CharField(max_length=500,db_column='add_line')
    city = models.CharField(max_length=100,db_column='city')
    contact_no = models.CharField(max_length=50,db_column='contact_no')
    department = models.ForeignKey(Department,on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'emp'

    def __str__(self):
        return self.name

class Customer(models.Model):
    id = models.CharField(max_length=4,primary_key=True,db_column='cust_id')
    name = models.CharField(max_length=100,db_column='cust_name',unique=True)
    credit_limit = models.DecimalField(max_digits=2,decimal_places=0,db_column='credit_limit')
    address = models.CharField(max_length=255,db_column='address')
    landmark = models.CharField(max_length=255, db_column='landmark')
    city = models.CharField(max_length=50, db_column='city')
    state = models.CharField(max_length=50, db_column='state')

    class Meta:
        db_table = 'customer'

    def __str__(self):
        return self.name

class Product(models.Model):
    id = models.CharField(max_length=4,primary_key=True,db_column='product_id')
    name = models.CharField(max_length=100,db_column='product_name',unique=True)
    manufacturer = models.CharField(max_length=100,db_column='manufacturer')
    cost_rate = models.DecimalField(max_digits=12,decimal_places=2,db_column='cost_rate')

    class Meta:
        db_table = 'product'

    def __str__(self):
        return self.name