from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from users.models import *
from users.serializers import *
# Create your views here

@crsf_exempt
def user_list(request):
	if request.method == "GET":
		user_l = User.objects.all()
		serializer = UserSerializer(user_l, many=True)
		return JsonResponse(serializer.data, safe=False)

	elif request.method == "POST":
		data = JSONParser().parse(request)
		serializer = UserSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data, status=201)
		return JsonResponse(serializer.errors, status=400)

@crsf_exempt
def user_detail(request, pk):
	try:
		user = User.objects.get(pk = pk)
	except User.DoesNotExist:
		return HttpResponse(status = 404)

	if request.method == "GET":
		serializer = UserSerializer(user)
		return JsonResponse(serializer.data)

	elif request.method == "PUT":
		data = JSONParser().parse(request)
		serializer = UserSerializer(user, data = data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializers.data)
		return JsonResponse(serializer.errors, status = 400)
	elif request.method == "DELETE":
		user.delete()
		return HttpResponse(status = 204)

