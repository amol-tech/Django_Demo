from django import forms
from app_demo.models import Employee,Sales,SalesItem,Customer
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit,Field

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

class SalesForm(forms.ModelForm):
    class Meta():
        model = Sales
        fields = '__all__'

    date = forms.DateField(localize=True, widget=DateInput)

class SalesItemForm(forms.ModelForm):

    class Meta():
        model = SalesItem
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(SalesItemForm, self).__init__(*args, **kwargs)
        self.fields['sales'] .disabled = True

class CustomerForm(forms.ModelForm):
    class Meta():
        model = Customer
        fields = '__all__'

