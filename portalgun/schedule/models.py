from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Event(models.Model):
    name = models.CharField(max_length=100)
    time = models.TimeField()
    duration = models.DurationField()
    location = models.CharField(max_length=100)
    password = models.CharField(max_length=20, blank=True)
    description = models.TextField(null=True, blank=True)
    successtext = models.TextField(null=True, blank=True)
    event_img = models.ImageField(upload_to='images/events/',
                                  null=True,
                                  blank=True)

    def __str__(self):
        return self.name + self.time.strftime(" (%I:%M)")

    class Meta:
        ordering = ('time', 'name',)


class Schedule(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    revealed = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user) + ' at ' + str(self.event)
