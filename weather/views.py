
from django.shortcuts import render
import requests
import geocoder
from .models import *
from django.contrib.gis.geos import fromstr

# Create your views here.
def index(request):
     if request.method == "POST":
          address= request.POST['city']

          location = geocoder.osm(address)
          lat = location.lat
          lng= location.lng
          latlng = location.latlng
          
          


          # creating map object
          
          url='http://api.openweathermap.org/data/2.5/weather?q=' +address + '&units=metric&appid=01e194711876a2a9cf8c1463025d0999'
          r = requests.get(url.format(address)).json()

          data = {
               "country_code": str(r['sys']['country']),
               'city':address,
               "coordinate": str(r['coord']['lon']) + ','
                             + str(r['coord']['lat']),
               "temp": str(r['main']['temp']) + '°C',
               "pressure": str(r['main']['pressure']),
               "humidity": str(r['main']['humidity']),
               "main": str(r['weather'][0]['main']),
               "description": str(r['weather'][0]['description']),
               "icon": str(r['weather'][0]['icon']),
               'map': map,
               'latlng': latlng,
               'lat': lat,
               'lng': lng,
          }
          
          weather = Weather(
          
          city=address,
          location=fromstr(f'POINT({lat} {lng})', srid=4326),
          tempreature=r['main']['temp'],
          pressure=r['main']['pressure'],
          humidity=r['main']['humidity'],
          forecast=r['weather'][0]['main'],
          description=r['weather'][0]['description'])

          weather.save()


          
          
          
     else:
          return render(request,'index.html')

     return render(request,'index.html',data)
