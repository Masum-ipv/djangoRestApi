# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render

# from django.http import HttpResponse
# from django.views import View
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import status
from country.models import City
from .serializers import Cityserializer
# Create your views here.

class CityList(APIView):
# class CityList(View):

	def get(self, request, name=''):
		if name:
			citys = City.objects.all().filter(capital=name)
		else:
			citys = City.objects.all()
		serializer = Cityserializer(citys, many=True)
		return Response(serializer.data)

	# def get(self, request, *args, **kwargs):
	# 	print(args)
	# 	print(kwargs)
	# 	citys = City.objects.get(kwargs)
	# 	serializer = Cityserializer(citys, many=True)
	# 	return HttpResponse(serializer.data)