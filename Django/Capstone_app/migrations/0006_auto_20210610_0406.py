# Generated by Django 3.2.3 on 2021-06-10 04:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Capstone_app', '0005_task_task_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='proposal',
            name='project_date_end',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='proposal',
            name='project_date_start',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]
