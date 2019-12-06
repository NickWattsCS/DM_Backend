from django.db import models
"""
Leaderboard for actual app
"""

class BarGraph(models.Model):
    name = models.CharField(max_length = 100, default = 'Group')
    amount = models.IntegerField(default = 0)
    position = models.IntegerField(default = 0)
    horizontal = models.BooleanField(default = True)

    class Meta:
        ordering = ('name',)

class PieGraph(BarGraph):
    color = models.CharField(max_length = 10, default = '#000000')
    legendFontColor = models.CharField(max_length = 8, default = '#000000')
    legendFontSize = models.IntegerField(default = 15)

    class Meta:
        ordering = ('name',)
