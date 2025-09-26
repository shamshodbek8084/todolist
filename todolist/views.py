from django.shortcuts import render
from .models import todos
from .serializers import todoSerializer
from rest_framework import generics

# Create your views here.
class ListView(generics.ListAPIView):
    queryset = todos.objects.all()
    serializer_class = todoSerializer

class DetailIdView(generics.RetrieveAPIView):
    queryset = todos.objects.all()
    serializer_class = todoSerializer