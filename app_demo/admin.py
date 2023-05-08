from django.contrib import admin
from app_demo.models import Department,Employee,Customer,Product

# Register your models here.
admin.site.register(Department)
admin.site.register(Employee)
admin.site.register(Customer)
admin.site.register(Product)
