# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-14 04:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('laptop', '0003_auto_20170513_2216'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='incidente',
            name='laptop',
        ),
        migrations.AddField(
            model_name='incidente',
            name='laptop',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='laptop.Laptop'),
            preserve_default=False,
        ),
    ]
