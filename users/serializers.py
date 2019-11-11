from rest_framework import serializers
from users.models import DanceUser,Dancer,DanceStaff,DanceGuest

class DanceUserSerializer(serializers.ModelSerializer):
	class Meta:
		model = DanceUser
		fields = ["id", "first_name", "last_name", "email", "date_joined", "last_login", "organization", "mon_raised"]

class DancerSerializer(serializers.ModelSerializer):
	class Meta:
		model = Dancer
		fields = ["id", "first_name", "last_name", "email", "date_joined", "last_login", "organization", "mon_raised"]

class DanceStaffSerializer(serializers.ModelSerializer):
	class Meta:
		model = DanceStaff
		fields = ["id", "first_name", "last_name", "email", "date_joined", "last_login", "organization", "mon_raised"]
"""

I will work on this model after I get the others to work

class DanceGuestSerializer(serializers.ModelSerializers):
	class Meta:
		model = DanceGuest
		fields = ["date_joined"]
"""
