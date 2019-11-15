from django.db import models
from users.models import DanceUser
"""
Organization name and total points
"""
class DanceGroup(models.Model):
    name = models.CharField(max_length = 100)
    mon_raised = models.IntegerField(default=0)
    points = models.IntegerField(default=0)
    users = models.ManyToManyField(DanceUser)

    class Meta:
        ordering = ('name',)
