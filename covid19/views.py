from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, ListAPIView, DestroyAPIView

from .models import Covid19
from .serializers import covid19Serializer

# Create your views here.


class CreateRecords(ListCreateAPIView):
    queryset  = Covid19.objects.all()
    serializer_class = covid19Serializer

class ViewRecords(ListAPIView):
    queryset = Covid19.objects.all()
    serializer_class = covid19Serializer

class DeleteRecords(DestroyAPIView):
    queryset = Covid19.objects.all()
    serializer_class = covid19Serializer