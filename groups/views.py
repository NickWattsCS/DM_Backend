from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
import csv

from django.http import HttpResponse
from rest_framework import viewsets
from .models import DanceGroup
from .serializers import GroupSerializer

class GroupViewSet(viewsets.ModelViewSet):
    queryset = DanceGroup.objects.all().order_by("mon_raised")
    serializer_class = GroupSerializer

@admin.register(DanceGroup)
class ViewGroups(ImportExportModelAdmin):
    pass
