from .models import Groups
from rest_framework import serializers

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name', 'mon_raised', 'points']
        read_only_fields = ('id', 'name', 'mon_raised', 'points')
