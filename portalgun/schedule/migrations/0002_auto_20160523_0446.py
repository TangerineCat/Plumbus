# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-23 11:46
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('schedule', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schedule',
            name='event',
        ),
        migrations.AddField(
            model_name='schedule',
            name='event',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='schedule.Event'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='user',
        ),
        migrations.AddField(
            model_name='schedule',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
