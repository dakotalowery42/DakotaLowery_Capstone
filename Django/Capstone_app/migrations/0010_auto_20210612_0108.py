# Generated by Django 3.2.3 on 2021-06-12 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Capstone_app', '0009_auto_20210611_0421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proposal',
            name='project_date_end',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='proposal',
            name='project_date_start',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='task',
            name='gantt_date_end',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='task',
            name='gantt_date_start',
            field=models.DateField(),
        ),
    ]
