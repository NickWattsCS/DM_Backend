import csv

from django.http import HttpResponse
from rest_framework import viewsets
from .models import DanceGroup
from .serializers import GroupSerializer

class GroupViewSet(viewsets.ModelViewSet):
    queryset = DanceGroup.objects.all()
    serializer_class = GroupSerializer

def export_DanceGroups_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="DanceGroups.csv"'

    writer = csv.writer(response)
    writer.writerow(['Group', 'Funds Raised', 'Points'])

    DanceGroups = DanceGroup.objects.all().values_list('name', 'mon_raised', 'points')
    for DanceGroup in DanceGroups:
        writer.writerow(DanceGroup)

    return response
