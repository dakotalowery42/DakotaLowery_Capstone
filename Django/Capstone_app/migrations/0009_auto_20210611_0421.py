# Generated by Django 3.2.3 on 2021-06-11 04:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Capstone_app', '0008_auto_20210611_0419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='gantt_date_end',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='task',
            name='gantt_date_start',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]
