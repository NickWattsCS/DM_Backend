from rest_framework import serializers

from .models import Event

class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = ('id', 'name', 'time', 'place', 'code', 'points', 'description')
        read_only_fields = ('id',)
