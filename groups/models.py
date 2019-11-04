from django.db import models
"""
Organization name and total points
"""
class Groups(models.Model):
    name = models.CharField(max_length = 100)
    mon_raised = models.IntegerField(default=0)
    points = models.IntegerField(default=0)

    class Meta:
        ordering = ('name',)
