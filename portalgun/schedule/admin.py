from django.contrib import admin

# Register your models here.
from .models import Event, Schedule

admin.site.register(Event)
admin.site.register(Schedule)
