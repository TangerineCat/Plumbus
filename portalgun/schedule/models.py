from __future__ import unicode_literals

from django.db import models
from info.models import Team


class Event(models.Model):
    name = models.CharField(max_length=100)
    time = models.TimeField()
    location = models.CharField(max_length=100)
    password = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.name + self.time.strftime(" (%I:%M)")

    class Meta:
        ordering = ('time',)


class Schedule(models.Model):
    user = models.ManyToManyField(Team)
    event = models.ManyToManyField(Event)

    def __str__(self):
        return self.user + 'at' + self.event
