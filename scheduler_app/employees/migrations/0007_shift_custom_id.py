# Generated by Django 4.1.7 on 2023-11-02 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0006_shift_repeat_shift_repeat_interval_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='shift',
            name='custom_id',
            field=models.CharField(default='', editable=False, max_length=16),
        ),
    ]
