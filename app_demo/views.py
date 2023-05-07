from django.shortcuts import render
from app_demo.models import Employee
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from app_demo.forms import EmployeeForm
from django.urls import reverse,reverse_lazy

# All Index Base View Here .....................................................................
def index_main(request):
  return render(request, 'app_demo/main.html')



# All Class Base View Here ......................................................................

class EmployeeListView(ListView):
    model = Employee
    template_name = 'app_demo/list_employee.html'
    # employee_list is the variable generated by ListVIew model

class EmployeeCreateView(CreateView):
    form_class = EmployeeForm
    model = Employee
    template_name = 'app_demo/detail_employee.html'
    success_url = reverse_lazy('app_demo:index_employees')

class EmployeeUpdateView(UpdateView):
    form_class = EmployeeForm
    model = Employee
    template_name = 'app_demo/detail_employee.html'
    success_url = reverse_lazy('app_demo:index_employees')

class EmployeeDeleteView(DeleteView):
    model = Employee
    template_name = 'app_demo/delete_any.html'
    success_url = reverse_lazy('app_demo:index_employees')
