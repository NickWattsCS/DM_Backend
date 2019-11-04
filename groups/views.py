from rest_framework import viewsets
from .models import Groups
from .serializers import GroupSerializer

class GroupsViewset(generics.ModelViewSet):
    queryset = AdminGroup.objects.all().order_by("name")
    serializer_class = GroupSerializer
