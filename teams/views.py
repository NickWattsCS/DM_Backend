import csv

from django.shortcuts import render
from rest_framework import viewsets
from django.http import HttpResponse
from .models import Team
from .serializers import TeamSerializer

# Create your views here.

class TeamViewSet(viewsets.ModelViewSet):
	queryset = Team.objects.all().order_by("child")
	serializer_class = TeamSerializer

