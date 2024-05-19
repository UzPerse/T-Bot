from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework.views import exception_handler
from .models import *
from .serializers import *


# Store data API View
class StoreDetailView(generics.ListAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializers