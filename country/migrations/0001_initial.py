# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-16 08:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('capital', models.CharField(max_length=250)),
                ('countryName', models.CharField(max_length=250)),
            ],
        ),
    ]
