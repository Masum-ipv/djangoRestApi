# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class City(models.Model):
	capital = models.CharField(max_length=250)
	countryName = models.CharField(max_length=250)

	def __str__(self):
		return self.capital