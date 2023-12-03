from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Employee, Calendar, Shift, Day
from .forms import EmployeeForm, CalendarForm, ShiftForm, EmployeeSelectionForm
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
import datetime, random, string
from .functions import get_today
from .brain import create_shifts_model




# Create your views here.
def home(request):
    return render(request, "base.html")

class EmployeeView(ListView):
    model = Employee
    template_name = "employees.html"
    context_object_name = 'employees'


class EmployeeCreate(CreateView):
    model = Employee
    template_name = "employee_create_form.html"
    form_class = EmployeeForm
    success_url = reverse_lazy("employees")
    

class EmployeeUpdate(UpdateView):
    model = Employee
    template_name = "employee_update_form.html"
    form_class = EmployeeForm
    success_url = reverse_lazy("employees")
    context_object_name = 'employee'

class EmployeeDelete(DeleteView):
    model = Employee
    template_name = "employee_delete_form.html"
    success_url = reverse_lazy("employees")
    context_object_name = 'employee'


class CalendarView(ListView):
    model = Calendar
    template_name = "calendars.html"
    context_object_name = 'calendars'


class CalendarCreate(CreateView):
    model = Calendar
    template_name = "calendar_create_form.html"
    form_class = CalendarForm
    success_url = reverse_lazy("calendars")
    

class CalendarUpdate(UpdateView):
    model = Calendar
    template_name = "calendar_update_form.html"
    form_class = CalendarForm
    success_url = reverse_lazy("calendars")
    context_object_name = 'calendar'

class CalendarDelete(DeleteView):
    model = Calendar
    template_name = "calendar_delete_form.html"
    success_url = reverse_lazy("calendars")
    context_object_name = 'calendar'



class ShiftView(ListView):
    model = Shift
    template_name = "shifts.html"
    context_object_name = 'shifts'


class ShiftCreate(CreateView):
    model = Shift
    template_name = "shift_create_form.html"
    form_class = ShiftForm
    success_url = reverse_lazy("calendars")
    

def shift_create(request, date=None):
    if date is None:
        date_obj = get_today()
    else:
        date_obj = datetime.datetime.strptime(date, '%Y-%m-%d').date()
    
    if request.method == 'POST':
        form = ShiftForm(request.POST)
        if form.is_valid():

            updated_date = form.cleaned_data.get('date')
            # Update the day_instance based on the updated date
            day_instance = get_object_or_404(Day, date=updated_date)

            shift_instance = form.save(commit=False)
            shift_instance.shifts_in_day = day_instance

            shift_instance.custom_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=16))


            shift_instance.save()

            if shift_instance.repeat == True: 
                new_date = shift_instance.shifts_in_day.date + datetime.timedelta(days=shift_instance.repeat_interval)
                while (shift_instance.shifts_in_day.days_in_calendar.end_date) >= new_date:
                    repeated_shift_instance = Shift.objects.create(
                    start_time = shift_instance.start_time,
                    end_time = shift_instance.end_time,
                    custom_id = shift_instance.custom_id,
                    repeat = False,
                    shifts_in_day = get_object_or_404(Day, date=new_date))
                    new_date += datetime.timedelta(days=shift_instance.repeat_interval)
                    repeated_shift_instance.save()
            calendar_view_url = reverse('calendars')
            return redirect(calendar_view_url)
        else: 
            form = ShiftForm(initial={'date': date_obj})

        return render(request, 'shift_create_form.html', {'form': form})


class ShiftUpdate(UpdateView):
    model = Shift
    template_name = "shift_update_form.html"
    form_class = ShiftForm
    success_url = reverse_lazy("shifts")
    context_object_name = 'shift'

    def get_initial(self):
        # Get the initial values for the form fields
        initial = super().get_initial()
        # Retrieve the date from the URL parameters and set it as the initial value for the 'date' field
        initial['date'] = self.kwargs['date']
        return initial

class ShiftDelete(DeleteView):
    model = Shift
    template_name = "shift_delete_form.html"
    context_object_name = 'shift'
    success_url = reverse_lazy('calendars')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        custom_id = self.get_object().custom_id
        other_shifts_with_custom_id = Shift.objects.filter(custom_id=custom_id).exclude(pk=self.get_object().pk)
        context['other_shifts_with_custom_id'] = other_shifts_with_custom_id
        return context

    def form_valid(self, form):
        confirm_delete = self.request.POST.get('confirm_delete')
        print(confirm_delete)
        if confirm_delete == 'Delete All Instances':
            custom_id = self.get_object().custom_id
            shifts_to_delete = Shift.objects.filter(custom_id=custom_id).delete()
            # Redirect to the success URL after deleting all instances
            return redirect(self.success_url)
        # Proceed with the delete operation for the current instance
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("calendars")
    

def process_selection(request, calendar_id):
    if request.method == 'POST':
        
        form = EmployeeSelectionForm(request.POST)
        if form.is_valid():
            selected_employees = form.cleaned_data['employees']

            chosen_calendar = get_object_or_404(Calendar, id=calendar_id)
            number_of_days_in_calendar = (chosen_calendar.end_date - chosen_calendar.start_date).days + 1 # 1 added because it counts from 0
            days_in_calendar_list = list(Day.objects.filter(days_in_calendar__id = calendar_id))
            shifts_in_calendar = Shift.objects.filter(shifts_in_day__days_in_calendar__id = calendar_id)
            number_of_shifts_in_calendar = len(shifts_in_calendar)
            number_of_employees_in_work = len(selected_employees)

            critical_days_array = []

            #Make array with day as index and shift as key on index
            for day in days_in_calendar_list: 
                current_day_shifts = day.shifts.all()
                critical_days_array.append({shift:list(selected_employees) for shift in current_day_shifts}) #Creates array with all shifts every index is a day from start_date
            
            #Remove employees from days they cant work
            for employee in selected_employees:
                #if employee has weeks not workable with weeknumbers
                if employee.weeks_off:
                    weeks = employee.weeks_off.split(",")
                    
                    for week in weeks:
                        #is not removing week 1 due to more weeks being present. 
                        stripped_week = week.strip()
                        year = chosen_calendar.start_date.year
                        first_day = datetime.datetime.strptime(f'{year}-W{stripped_week}-1', '%Y-W%W-%w').date()
                        #Finds first instance of day-instance with day-attribute equal to first_day
                        index_of_day_target = next((index for index, day_instance in enumerate(days_in_calendar_list) if day_instance.date == first_day), None)
                        #Removes employee from the week it cannot work
                        
                        if index_of_day_target != None:
                            for x in range(7):
                                
                                #removes employee from shifts next 7 days
                                try:
                                    for key, value in critical_days_array[index_of_day_target + x].items():
                                        if employee in value:
                                            critical_days_array[index_of_day_target + x][key].remove(employee)
                                except:
                                    continue
                
                #If employee has a time-period notworkable in date-format
                if employee.time_periods_off:
                    
                    periods = employee.time_periods_off.split(",")
                    for period in periods: 
                        start_end_dates = period.split(":")
                        
                        start_date_TimePeriodOff = start_end_dates[0].strip()
                        end_date_TimePeriodOff = start_end_dates[1].strip()
                        start_date_object_TimePeriodOff = datetime.datetime.strptime(start_date_TimePeriodOff, "%Y-%m-%d").date()
                        end_date_object_TimePeriodOff = datetime.datetime.strptime(end_date_TimePeriodOff, "%Y-%m-%d").date()

        
                        index_of_day_start_target_TimePeriodOff = next((index for index, day_instance in enumerate(days_in_calendar_list) if day_instance.date == start_date_object_TimePeriodOff), None)
                        
                        index_range_TimePeriodOff = (end_date_object_TimePeriodOff - start_date_object_TimePeriodOff).days
                        
                        if index_of_day_start_target_TimePeriodOff:
                            for x in range(index_range_TimePeriodOff):
                                for key, value in critical_days_array[index_of_day_start_target_TimePeriodOff + x].items():
                                    if employee in value:
                                        critical_days_array[index_of_day_start_target_TimePeriodOff + x][key].remove(employee)

                        
                # If employee has individual days not workable 
                if employee.individual_days_off:
                    
                    days = employee.individual_days_off.split(",")
                    for day in days: 
                        day_to_search_IndividualDaysOff = day.strip()
                        day_to_search_object_IndividualDaysOff = datetime.datetime.strptime(day_to_search_IndividualDaysOff, "%Y-%m-%d").date()
                        index_to_remove_IndividualDaysOff = next((index for index, day_instance in enumerate(days_in_calendar_list) if day_instance.date == day_to_search_object_IndividualDaysOff), None)
                        if index_to_remove_IndividualDaysOff:
                            for key, value in critical_days_array[index_to_remove_IndividualDaysOff].items():
                                    if employee in value:
    
                                        critical_days_array[index_to_remove_IndividualDaysOff][key].remove(employee)

            #Now that employees are added to the days they can it should start to fill upp with workers starting with the lowest ones first: 
            
            print(critical_days_array)
            shift_model = create_shifts_model(critical_days_array)
            print(shift_model)

            #sorted_shifts = sorted(critical_days_array, key=lambda shift_dict: min(len(employees) for employees in shift_dict.values()))
            #for shift in sorted_shifts:
                #print(shift)
            

            calendar_view_url = reverse('calendars')
            return redirect(calendar_view_url)
    else:
        form = EmployeeSelectionForm()

    return render(request, 'fill_create_form.html', {'form': form})
    