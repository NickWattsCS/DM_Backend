from rest_framework import viewsets
from users.models import *
from users.serializers import *
# Create your views here

class DanceUserViewSet(viewsets.ModelViewSet):
	queryset = DanceUser.objects.all().order_by("id")
	serializer_class = DanceUserSerializer

def mon_raised(request):
	sum = 0
	for person in DanceUser.objects.all():
		sum = sum + person.getMoney()
	return HttpResponse("<html><h1>All users have raised %s in total.<h1><html>" % sum)
