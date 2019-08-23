# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class location(models.Model):
    lat = models.DecimalField( max_digits=7, decimal_places=4)  
    lon = models.DecimalField(max_digits=7,decimal_places=4)
    city = models.CharField(max_length=255, null=False)
    state =  models.CharField(max_length=255, null=False)
     
class weather(models.Model):
    id = models.IntegerField(primary_key=True,unique=True,auto_created=False)
    date = models.DateField()
    location = models.ForeignKey("location")
    
class temperature(models.Model):
    weather = models.ForeignKey("weather")
    temperature = models.DecimalField( max_digits=3, decimal_places=1) 
    def __str__(self):
        return '%s' % (self.temperature) 






