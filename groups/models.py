from django.db import models
from teams.models import Team

class DanceGroup(models.Model):
    name = models.CharField(max_length = 100)
    mon_raised = models.IntegerField(default=0)
    points = models.IntegerField(default=0)
    team = models.ForeignKey(Team, related_name="dance_team", null = True, on_delete = models.CASCADE)

    class Meta:
        ordering = ('name',)

