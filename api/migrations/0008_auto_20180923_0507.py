# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-09-23 05:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20180923_0504'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mass',
            options={'verbose_name': 'Missa'},
        ),
        migrations.AddField(
            model_name='mass',
            name='massMoments',
            field=models.ManyToManyField(to='api.MassMoment'),
        ),
    ]