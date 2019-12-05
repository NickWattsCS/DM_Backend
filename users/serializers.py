from rest_framework import serializers
from .models import DanceUser
from django.conf import settings
from rest_auth.registration.serializers import RegisterSerializer
from rest_auth.serializers import LoginSerializer
from rest_auth.models import TokenModel
from allauth.account.adapter import get_adapter

class DanceUserSerializer(serializers.ModelSerializer):
	class Meta:
		model = DanceUser
		fields = ("id", "first_name", "last_name", "email", "date_joined", "last_login")
		read_only_fields = ('id',)

class CustomRegisterSerializer(RegisterSerializer):
    organization = serializers.CharField()

    class Meta:
        model = DanceUser
        fields = ('email', 'username', 'password', 'organization')

    def get_clean_data(self):
        return {
                'username': self.validate_data.get('username', ''),
                'password1': self.validate_data.get('password1', ''),
                'password2': self.validate_data.get('password2', ''),
                'email': self.validate_data.get('email', ''),
                'organization': self.validate_Data.get('organization', '')
        }

        def save(self, request):
            adapter = get_adapter()
            user = adapter.new_user(request)
            self.cleaned_data = self.get_clean_data()
            user.organization = self.cleaned_data.get('organization')
            user.save()
            adapter.save_user(request, user, self)
            return user

class LoginSerializer(LoginSerializer):
    def get_fields(self):
        fields = super(LoginSerializer, self).get_fields()
        fields['email'] = fields['username']
        del fields['username']
        return fields

    def validate(self, attrs):
        attrs['username'] = attrs['email']
        del attrs['email']
        return super(LoginSerializer, self).validate(attrs)

class TokenSerializer(serializers.ModelSerializer):
    user = DanceUserSerializer(many=False, read_only=True)

    class Meta:
        model = TokenModel
        fields = ['key', 'user']
