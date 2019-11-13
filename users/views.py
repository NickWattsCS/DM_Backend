from rest_framework import viewsets
from users.models import *
from users.serializers import *
# Create your views here

class DanceUserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all().order_by("last_name")
	serializer_class = UserSerializer

