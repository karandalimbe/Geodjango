from django.db import models

from django.contrib.gis.db import models

# Create your models here.
class Weather(models.Model):
    
    city = models.CharField(max_length=20)
    location=models.PointField(srid=4326)
    tempreature = models.CharField(max_length=20)
    pressure =models.IntegerField()
    humidity = models.IntegerField()
    forecast = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    
