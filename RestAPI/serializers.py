from __future__ import unicode_literals
from rest_framework import serializers
from .models import weather,location,temperature

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = location
        fields = ("lat", "lon", "city", "state")
    

class WeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = weather
        fields = ("location","id","date")

class TemperatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = temperature
        fields = ("weather","temperature") 
