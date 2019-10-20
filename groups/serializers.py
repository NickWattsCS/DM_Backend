from groups.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import Group
from rest_framework import serializers

class AdminGroupList(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = AdminGroup
        fields = ['id', 'username', 'firstName', 'lastName', 'permissions']

class StaffGroupDetail(serializers.ModelSerializer):
    class Meta:
        model = StaffGroup
        fields = ['id', 'username', 'firstName', 'lastName', 'permissions']

class UserGroupDetail(serializers.ModelSerializer):
    class Meta:
        model = UserGroup
        fields = ['id', 'username', 'firstName', 'lastName', 'permissions']
