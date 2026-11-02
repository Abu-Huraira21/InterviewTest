from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .serailizers import EventsSerializer
from .models import Events

class EventViewSet(viewsets.ModelViewSet):
    queryset = Events.objects.all()
    serializer_class = EventsSerializer