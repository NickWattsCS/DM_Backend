from rest_framework import viewsets
from rest_framework.authtoken.views import ObtainAuthToken
from users.models import *
from users.serializers import *
from django.contrib.auth import get_user_model

# Create your views here

class DanceUserViewSet(viewsets.ModelViewSet):
	queryset = get_user_model().objects.all()
	serializer_class = DanceUserSerializer

def mon_raised(request):
	sum = 0
	for person in DanceUser.objects.all():
		sum = sum + person.getMoney()
	return HttpResponse("<html><h1>All users have raised %s in total.<h1><html>" % sum)

class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })
