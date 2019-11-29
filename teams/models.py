from django.db import models

class Team(models.Model):
	child = models.CharField(max_length = 20, null = True)
	mon_raised = models.IntegerField(default = 0)

