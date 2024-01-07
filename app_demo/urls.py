from django.urls import path,re_path
from app_demo import views

app_name = 'app_demo'

urlpatterns = [
    path('main/', views.index_main, name='index_main'),
    path('context_menu/<str:pk>/', views.index_context_menu, name='index_context_menu'),
    path('courses/', views.index_courses, name='index_courses'),
    # Urls for Employee .....................................................................................
    path('employees/', views.index_employees, name='index_employees'),
    path('employee_create/', views.EmployeeCreateView.as_view(), name='index_employee_create'),
    path('employee_update/<str:pk>/', views.EmployeeUpdateView.as_view(), name='index_employee_update'),
    path('employee_delete/<str:pk>/', views.EmployeeDeleteView.as_view(), name='index_employee_delete'),
    # Urls for Sales ........................................................................................
    path('sales_tree/', views.index_sales_tree, name='index_sales_tree'),
    path('sales_list/', views.index_sales_list, name='index_sales_list'),
    path('sales_detail/<str:sales_id>/', views.index_sales_master_detail, name='index_sales_master_detail'),
    path('sales_update/<str:pk>/', views.SalesUpdateView.as_view(), name='index_sales_update'),
    path('sales_delete/<str:pk>/', views.SalesDeleteView.as_view(), name='index_sales_delete'),
    # Urls for SalesItem ....................................................................................
    path('sales_item_list/', views.index_sales_item_list, name='index_sales_item_list'),
    path('salesitem_create/<str:fk>/', views.SalesItemCreateView.as_view(), name='index_salesitem_create'),
    path('salesitem_update/<str:pk>/', views.SalesItemUpdateView.as_view(), name='index_salesitem_update'),
    path('salesitem_delete/<str:pk>/', views.SalesItemDeleteView.as_view(), name='index_salesitem_delete'),
    # Urls for Customer .....................................................................................
    path('customers/', views.CustomerListView.as_view(), name='index_customers'),
    path('customer_create/', views.CustomerCreateView.as_view(), name='index_customer_create'),
    path('customer_update/<str:pk>/', views.CustomerUpdateView.as_view(), name='index_customer_update'),
    path('customer_delete/<str:pk>/', views.CustomerDeleteView.as_view(), name='index_customer_delete'),
]