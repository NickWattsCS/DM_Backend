from rest_framework import serializers
from .models import DanceUser

class DanceUserSerializer(serializers.ModelSerializer):
	class Meta:
		model = DanceUser
		fields = ["id", "first_name", "last_name", "email", "date_joined", "last_login"]
