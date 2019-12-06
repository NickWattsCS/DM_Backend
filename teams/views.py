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

def export_Teams_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="DM_Teams.csv"'

    writer = csv.writer(response)
    writer.writerow(['Team', 'Funds Raised'])

    Teams = Team.objects.all().values_list('child', 'mon_raised')
    for Team in Teams:
        writer.writerow(Team)

    return response
