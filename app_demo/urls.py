from django.urls import path,re_path
from app_demo import views

app_name = 'app_demo'

urlpatterns = [
    path('main/', views.index_main, name='index_main'),
    path('employees/', views.EmployeeListView.as_view(), name='index_employees'),
]