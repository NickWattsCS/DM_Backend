import csv 
from django.contrib import admin                                                                                                                              
from import_export.admin import ImportExportModelAdmin 

from django.http import HttpResponse
from rest_framework import viewsets
from .models import DanceGroup
from .serializers import GroupSerializer

class GroupViewSet(viewsets.ModelViewSet):
    queryset = DanceGroup.objects.all().order_by("mon_raised")
    serializer_class = GroupSerializer

def export_DanceGroups_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="DM_DanceGroups.csv"'

    writer = csv.writer(response)
    writer.writerow(['Group', 'Funds Raised', 'Points'])

    DanceGroups = DanceGroup.objects.all().values_list('name', 'mon_raised', 'points')
    for item in DanceGroups:
        writer.writerow(item)

    return response

@admin.register(DanceGroup)                                                                                                                                   
class ViewGroups(ImportExportModelAdmin):                                                                                                                         
	pass
