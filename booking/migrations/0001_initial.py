# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-17 07:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('level', models.IntegerField()),
                ('room', models.IntegerField()),
                ('am_dept', models.CharField(max_length=258)),
                ('pm_dept', models.CharField(max_length=258)),
                ('am_surg', models.CharField(max_length=258)),
                ('pm_surg', models.CharField(max_length=258)),
            ],
        ),
    ]
