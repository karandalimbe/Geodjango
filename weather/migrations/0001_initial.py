# Generated by Django 3.2.11 on 2022-03-21 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Weather',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('countrycode', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=20)),
                ('location', models.CharField(max_length=20)),
                ('tempreature', models.CharField(max_length=20)),
                ('pressure', models.IntegerField()),
                ('humidity', models.IntegerField()),
                ('forecast', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=50)),
            ],
        ),
    ]
