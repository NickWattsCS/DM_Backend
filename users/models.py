import datetime
from django.db import models
from django.contrib.auth.models import User, AnonymousUser
# Create your models here.



"""
DanceUser is the abstract class from which its children inherit the data members:
team: which uses Group as a foreign key to store the team's name
position: which states the user's rank in the hierachy of DM members 
	(Dancer, Captain, Core, Exec)
events: contains all events the user has signed up for
"""
class DanceUser(User):
	team = models.ForeignKey(Group, null = True, blank = True, on_delete = models.CASCADE)
	position = models.CharField(max_length=15, default='Dancer')
	events = models.ManyToManyField(Event)
	shift = models.IntegerField(blank = True, default = 0)
"""
DanceStaff is the class that contains users that contain some level of authority in the
hierarchy of DanceMarathon. In other words, they're the Captains, Core, and Exec members
of DanceMarathon. 

Data members:
job_title: the position title given to the idividual.
points: the number of points that person has earned.
mon_raised: the amount of money the person has earned.
"""
class DanceStaff(DanceUser):
	job_title = models.CharField(max_length=50,default='')
	points = models.IntegerField(blank=True,default=0)
	mon_raised = models.IntegerField(blank=True,default=0)

class Dancer(DanceUser):
	points = models.IntegerField(blank=True,default=0)
	mon_raised = models.IntegerField(blank=True,default=0)
