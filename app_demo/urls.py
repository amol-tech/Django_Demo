from django.urls import path,re_path
from app_demo import views

app_name = 'app_demo'

urlpatterns = [
    path('main/', views.index_main, name='index_main'),
    # Urls for Employee .....................................................................................
    path('employees/', views.EmployeeListView.as_view(), name='index_employees'),
    path('employee_create/', views.EmployeeCreateView.as_view(), name='index_employee_create'),
    path('employee_update/<str:pk>/', views.EmployeeUpdateView.as_view(), name='index_employee_update'),
    path('employee_delete/<str:pk>/', views.EmployeeDeleteView.as_view(), name='index_employee_delete'),
    # Urls for Sales ........................................................................................
    path('sales/', views.SalesListView.as_view(), name='index_sales'),
    path('sales_detail/<str:sales_id>/', views.index_sales_master_detail, name='index_sales_master_detail'),
    path('sales_update/<str:pk>/', views.SalesUpdateView.as_view(), name='index_sales_update'),
    path('sales_delete/<str:pk>/', views.SalesDeleteView.as_view(), name='index_sales_delete'),
    # Urls for SalesItem ....................................................................................
    path('salesitem_create/<str:fk>/', views.SalesItemCreateView.as_view(), name='index_salesitem_create'),
    path('salesitem_update/<str:pk>/', views.SalesItemUpdateView.as_view(), name='index_salesitem_update'),
    path('salesitem_delete/<str:pk>/', views.SalesItemDeleteView.as_view(), name='index_salesitem_delete'),
]