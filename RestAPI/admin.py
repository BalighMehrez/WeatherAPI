# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import location,weather,temperature
# Register your models here.
admin.site.register(location)
admin.site.register(weather)
admin.site.register(temperature)