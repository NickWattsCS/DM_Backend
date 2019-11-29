from django.db import models
from teams.models import Team
from users.models import DanceUser

class DanceGroup(models.Model):
    name = models.CharField(max_length = 100)
    mon_raised = models.IntegerField(default=0)
    points = models.IntegerField(default=0)
    team = models.ForeignKey(Team, related_name="dance_team", null = True, on_delete = models.CASCADE)

    class Meta:
        ordering = ('name',)

    def getMoney(self):
        sum = 0
        for person in DanceUser.objects.all():
            if person.getOrg() == self.name:
                sum = sum + person.getMoney()
        return sum
