from rest_framework import viewsets
from users.models import *
from users.serializers import *
# Create your views here

class DanceUserViewSet(viewsets.ModelViewSet):
	queryset = DanceUser.objects.all().order_by("id")
	serializer_class = DanceUserSerializer

