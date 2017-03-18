from django.shortcuts import render
from app1.models import autorModel
from rest_framework import generics, filters
from rest_framework.response import *
from app1.serializers import AutorSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import django_filters.rest_framework


class AutorList(generics.ListCreateAPIView):

    queryset = autorModel.objects.all()
    serializer_class = AutorSerializer
    filter_backends =  (filters.SearchFilter,django_filters.rest_framework.DjangoFilterBackend,)
    filter_fields = ('categoria','autor')
    search_fields = ('categoria','autor')





# Create your views here.
class AutorVista(generics.ListCreateAPIView):
	queryset = autorModel.objects.all()
	serializer_class = AutorSerializer


		#return self.list(self,request)

class AutorDetalle(generics.RetrieveUpdateDestroyAPIView):

    queryset = autorModel.objects.all()
    serializer_class = AutorSerializer



# Create your views here.
