import datetime
from groups.models import DanceGroup
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


"""
DanceUser is the class from which its children inherit the data members:
team: which uses Group as a foreign key to store the team's name
position: which states the user's rank in the hierachy of DM members 
	(Dancer, Captain, Core, Exec)
events: contains all events the user has signed up for
"""
class DanceUser(User):
	team = models.ForeignKey(DanceGroup, null = True, blank = True, on_delete = models.CASCADE)
	position = models.CharField(max_length=15, default='Dancer')
	events = models.ManyToManyField(Event)
	shift = models.IntegerField(blank = True, default = 0)

