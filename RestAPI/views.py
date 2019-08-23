# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import viewsets
from .models import weather
from .serializers import WeatherSerializer

class WeatherViewSet(viewsets.ModelViewSet):
    queryset = weather.objects.all()
    serializer_class=WeatherSerializer
