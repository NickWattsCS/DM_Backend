from rest_framework import viewsets
from .models import DanceGroup
from .serializers import GroupSerializer

class GroupViewSet(viewsets.ModelViewSet):
    queryset = DanceGroup.objects.all().order_by("name")
    serializer_class = GroupSerializer
