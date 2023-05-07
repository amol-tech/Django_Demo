from django import forms
from app_demo.models import Employee

class DateInput(forms.DateInput):
    input_type = 'date'

class EmployeeForm(forms.ModelForm):
    desig_choices = (('Manager', 'Manager'),
                     ('Officer', 'Officer'),
                     ('Clerk', 'Clerk'),
                     ('Engineer', 'Engineer'),
                     ('Worker', 'Worker'),
                     ('Salesman', 'Salesman')
                     )

    joining_date = forms.DateField(localize=True, widget=DateInput)
    designation = forms.ChoiceField(choices=desig_choices)

    class Meta():
        model = Employee
        fields = '__all__'