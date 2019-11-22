from django.db import models
from users.models import getMoneyRaised

class Team(models.Model):
	child = CharField(max_length = 20, null = True)
	mon_raised = user.getMoneyRaised("team", child)
