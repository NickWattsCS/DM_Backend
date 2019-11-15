from django.contrib.auth.models import Group
from django.db import models
from users import models as usermodels
"""
Organization name and total points
"""
class DanceGroup(Group):
	name = models.CharField(max_length = 100)
	mon_raised = models.IntegerField(default=0)
	points = models.IntegerField(default=0)

	class Meta:
		ordering = ('name',)
