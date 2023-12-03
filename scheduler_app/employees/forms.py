from django import forms
from .models import Employee, Calendar, Shift

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"
    weeks_off = forms.CharField(initial='12,13,14')
    time_periods_off = forms.CharField(initial='2023-09-17 : 2023-09-23')
    individual_days_off = forms.CharField(initial='2023-09-17, 2023-09-18, 2023-09-20')


class CalendarForm(forms.ModelForm):
    class Meta:
        model = Calendar
        fields = "__all__"

class ShiftForm(forms.ModelForm):
    class Meta:
        model = Shift 
        fields = "__all__"
        exclude = ['shifts_in_day']
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

class EmployeeSelectionForm(forms.Form):
    employees = forms.ModelMultipleChoiceField(
        queryset=Employee.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
