# Generated by Django 3.2.11 on 2022-03-21 11:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0002_alter_weather_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='weather',
            name='countrycode',
        ),
    ]
