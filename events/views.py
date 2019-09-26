from rest_framework import viewsets
#from rest_framework.authentication import TokenAuthentication
#from rest_framework.permissions import IsAuthenticated

from .models import Event
from .serializers import EventSerializer

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
 #   authentication_classes = (TokenAuthentication,)
  #  permission_classes = (IsAuthenticated,)

# Create your views here.
