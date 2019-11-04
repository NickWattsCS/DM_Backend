from .models import Groups
from rest_framework import serializers

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['name', 'mon_raised', 'points']
        read_only_fields = ('id','mon_raised', 'points')
