from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Team(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    description = models.TextField(null=True)
    goal = models.TextField(null=True)
    team_img = models.ImageField(upload_to='images/teams/',
                                 null=True,
                                 blank=True)

    def __str__(self):
        return self.name


class Alignment(models.Model):
    NORMAL = 'N'
    COUNCILOFRICKS = 'C'
    RICKESTRICK = 'R'
    ALIGNMENT_CHOICES = (
        (NORMAL, 'Normal'),
        (COUNCILOFRICKS, 'Council of Ricks'),
        (RICKESTRICK, 'The Rickest Rick'),
    )
    alignment = models.CharField(
        max_length=1,
        choices=ALIGNMENT_CHOICES,
        default='N',
        primary_key=True
    )
    description = models.TextField(null=True)
    goal = models.TextField(null=True)
    badge_img = models.ImageField(upload_to='images/badges/',
                                  null=True,
                                  blank=True)

    def getAlignment(self):
        return [t[1] for t in self.ALIGNMENT_CHOICES
                if t[0] == self.alignment][0]

    def __str__(self):
        return self.getAlignment()


class Identity(models.Model):
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                primary_key=True)
    team = models.ForeignKey(Team)
    alignment = models.ForeignKey(Alignment)
    schmeckles = models.IntegerField(default=0)

    def __str__(self):
        return str(self.user)
