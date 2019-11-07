from rest_framework import viewsets
#from rest_framework.authentication import TokenAuthentication
#from rest_framework.permissions import IsAuthenticated

from models import PieGraph
from serializers import BarGraphSerializer, PieGraphSerializer

class PieGraphViewSet(viewsets.ModelViewSet):
    queryset = Graph.objects.all()
    serializer_class = PieGraphSerializer

class BarGraphViewSet(viewsets.ModelViewSet):
    queryset = Graph.objects.all()
    serializer_class = PieGraphSerializer
