# Generated by Django 3.2.5 on 2023-03-28 09:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Backend_Management_App', '0009_notice'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notice',
            name='notice_date',
        ),
    ]
