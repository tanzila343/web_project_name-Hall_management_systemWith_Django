# Generated by Django 3.2.5 on 2023-01-31 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Backend_Management_App', '0005_alter_attendance_attendence_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='attendence_date',
            field=models.DateField(),
        ),
    ]
