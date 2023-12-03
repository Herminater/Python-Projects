# Generated by Django 4.1.7 on 2023-10-23 15:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0002_shift_day_calendar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='calendar',
            name='days_in_calendar',
        ),
        migrations.RemoveField(
            model_name='day',
            name='shifts_in_day',
        ),
        migrations.AddField(
            model_name='day',
            name='calendar',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='employees.calendar'),
        ),
        migrations.RemoveField(
            model_name='shift',
            name='shifts_in_day',
        ),
        migrations.AddField(
            model_name='shift',
            name='shifts_in_day',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='employees.day'),
        ),
    ]
