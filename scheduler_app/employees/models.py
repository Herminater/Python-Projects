from django.db import models
from django.utils import timezone
import datetime
import random
import string 

# Create your models here.
class Employee(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    weeks_off = models.CharField(max_length=50, null=True, default=None)
    time_periods_off = models.CharField(max_length=50, null=True, default=None)
    individual_days_off = models.CharField(max_length=50, null=True, default=None)


    def __str__(self):
        return self.first_name + " " + self.last_name



class Calendar(models.Model):
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField(default=timezone.now)
    TRUE_FALSE_CHOICES = (
        (True, 'Yes'),
        (False, 'No'),
    )
    exclude_weekends = models.BooleanField(default=False, choices=TRUE_FALSE_CHOICES)
    exclude_individual_days = models.CharField(max_length=100)
    shifts_per_day = models.IntegerField(default=2)
    
    def save(self, *args, **kwargs):
        super(Calendar, self).save(*args, **kwargs)

        # Create Day instances and link them to the Calendar instance
        for x in range(0, (self.end_date - self.start_date).days + 1):
            date = self.start_date + datetime.timedelta(days=x)
            Day.objects.create(date=date, days_in_calendar=self)


        

    def __str__(self):
        return f"Calendar: {self.start_date.strftime('%Y-%m-%d')} - {self.end_date.strftime('%Y-%m-%d')}"
    
    
class Day(models.Model):
    date = models.DateField(default=timezone.now)
    days_in_calendar = models.ForeignKey(Calendar, on_delete=models.CASCADE, null=True, blank=True, related_name = "days") 
    
    def __str__(self):
        return self.date.strftime('%Y-%m-%d')

class Shift(models.Model):
    start_time = models.TimeField(default=datetime.time(12,0,0))    
    end_time = models.TimeField(default=datetime.time(12,0,0))
    shifts_in_day = models.ForeignKey(Day, on_delete=models.CASCADE, null=True, blank=True, related_name = "shifts")
    repeat = models.BooleanField(default=False)
    custom_id = models.CharField(max_length=16, editable=False, default = "")
    EVERY_DAY = 1
    EVERY_WEEK = 7
    EVERY_OTHER_WEEK = 14
    EVERY_4_WEEKS = 28

    INTERVAL_CHOICES = (
        (EVERY_DAY, 'Every day'),
        (EVERY_WEEK, 'Every week'),
        (EVERY_OTHER_WEEK, 'Every other week'),
        (EVERY_4_WEEKS, 'Every 4 weeks'),
    )

    repeat_interval = models.IntegerField(choices=INTERVAL_CHOICES, default=EVERY_DAY)

    

    def __str__(self):
        return f"{self.start_time.strftime('%H:%M')} - {self.end_time.strftime('%H:%M')}"
