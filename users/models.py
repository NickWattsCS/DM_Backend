from django.db import models
from django.contrib.auth.models import AbstractUser
from events.models import Event
from groups.models import DanceGroup
# Create your models here.


"""
DanceUser is the class from which its children inherit the data members:
team: which uses Group as a foreign key to store the team's name
position: which states the user's rank in the hierachy of DM members 
	(Dancer, Captain, Coordinator, Exec)
events: contains all events the user has signed up for
shift: contains the day in which the user will attend Dance Marathon
	(0 = no days, 1 = first shift, 2 = second shift, 3 = both shifts)
team: contains a foreign key to the Team model, which contains the name of the child of
	their team as well as the money they have raised
internal_team: the department in which the user belongs if they're not a Dancer.
"""
class DanceUser(AbstractUser):
	organization = models.ForeignKey(DanceGroup, related_name="group", null = True, on_delete=models.CASCADE)
	mon_raised = models.IntegerField(default = 0)
	position = models.CharField(max_length=15, null = True)
	events = models.ManyToManyField(Event, related_name="user_list", null = True)
	points = models.IntegerField(default = 0)
	shift = models.IntegerField(null = True)
	team = models.ForeignKey(Team, related_name="team", null = True, on_delete = models.CASCADE)
	internal_team = models.CharField(max_length = 30, null = True)
"""
	def addInternalTeam(self, i_team)
		if self.position != "Dancer":
			self.internal_team = i_team

"""

"""
This function will return the money raised by an organization, a team, an internal_team,
	a group of users, or the individual user based on the provided context and name.
So far this is just a skeleton with details to be added later.
"""
	def getMoneyRaised(self, context, name)
		if context == "organization":
		elif context == "team":
		elif context == "internal_team":
		elif context == "users":
		else:
			return self.mon_raised
