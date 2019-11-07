from rest_framework import serializers

from .models import BarGraph, PieGraph

class BarGraphSerializer(serializers.ModelSerializer):
    class Meta:
        name = models.CharField(max_length = 40)
        amount = models.IntegerField(default=0)
        horizontal = models.BooleanField(default=True)
        model = BarGraph
        fields = ('name', 'amount', 'horizontal')
        read_only_fields = ('name', 'amount', 'horizontal')

class PieGraphSerializer(serializers.ModelSerializer):
    class Meta:
        name = models.CharField(max_length = 40)
        amount = models.IntegerField(default=0)
        color = models.CharField(max_length = 10, default = '#000000')
        legendFontColor = models.CharField(max_length = 8, default = '#000000')
        legendFontSize = models.IntegerField(default = 15)
        model = PieGraph
        fields = ('name', 'amount', 'color', 'legendFontColor', 'legendFontSize')
        read_only_fields = ('name', 'amount', 'color', 'legendFontColor', 'legendFontSize')
