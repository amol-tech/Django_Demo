from django.urls import path,re_path
from app_demo import views

app_name = 'app_demo'

urlpatterns = [
    path('main/', views.index_main, name='index_main'),
    path('employees/', views.EmployeeListView.as_view(), name='index_employees'),
    path('employee_create/', views.EmployeeCreateView.as_view(), name='index_employee_create'),
    path('employee_update/<str:pk>/', views.EmployeeUpdateView.as_view(), name='index_employee_update'),
    path('employee_delete/<str:pk>/', views.EmployeeDeleteView.as_view(), name='index_employee_delete'),
]