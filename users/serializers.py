from rest_framework import serializers
from users.models import User,Dancer,Staff,Admin,Guest

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['id', 'first_name', 'last_name', 'joined', 'team']

class DancerSerializer(serializers.ModelSerializer):
	class Meta:
		model = Dancer
		fields = ['id', 'first_name', 'last_name', 'joined', 'team', 'points', 'mon_raised']

class StaffSerializer(serializers.ModelSerializer):
	class Meta:
		model = Staff
		fields = ['id', 'first_name', 'last_name', 'joined', 'team', 'points', 'mon_raised', 'department']

class AdminSerializer(serializers.ModelSerializer):
	class Meta:
		model = Admin
		fields = ['id', 'first_name', 'last_name', 'joined', 'team', 'points', 'mon_raised']

class GuestSerializer(UserSerializer):
	class Meta:
		model = Guest
		fields = ['id', 'joined']
