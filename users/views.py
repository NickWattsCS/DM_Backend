from rest_framework import viewsets
from users.models import *
from users.serializers import *
# Create your views here

class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all().order_by("last_name")
	serializer_class = UserSerializer

class DancerViewSet(viewsets.ModelViewSet):
	queryset = Dancer.objects.all().order_by("last_name")
	serializer_class = DancerSerializer

class StaffViewSet(viewsets.ModelViewSet):
	queryset = Staff.objects.all().order_by("last_name")
	serializer_class = StaffSerializer

class AdminViewSet(viewsets.ModelViewSet):
	queryset = Admin.objects.all().order_by("last_name")
	serializer_class = AdminSerializer

class GuestViewSet(viewsets.ModelViewSet):
	queryset = Guest.objects.all().order_by("joined")
	serializer_class = GuestSerializer
