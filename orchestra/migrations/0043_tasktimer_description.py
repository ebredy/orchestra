# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-19 22:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orchestra', '0042_mark_deleted_timeentries_no_worker'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasktimer',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
