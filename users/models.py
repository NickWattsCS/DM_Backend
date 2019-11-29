from django.db import models
from django.contrib.auth.models import AbstractUser
from events.models import Event
from groups.models import DanceGroup
from teams.models import Team
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
	events = models.ManyToManyField(Event, related_name="user_list")
	points = models.IntegerField(default = 0)
	shift = models.IntegerField(null = True)
	team = models.ForeignKey(Team, related_name="user_team", null = True, on_delete = models.CASCADE)
	internal_team = models.CharField(max_length = 30, null = True)

	def __str__():
		return self.first_name + " " + self.last_name

	def getMoney(self, context, name = "", list = list()):
		return self.mon_raised
					

	def getOrg(self):
		return self.organization.name

	def getTeam(self):
		return self.team.child

	def addInternalTeam(self, i_team):
		if self.position != "Dancer":
			self.internal_team = i_team
