from django.db import models

class User(models.Model):
	first_name = models.CharField(max_length = 30)
	last_name = models.CharField(max_length = 30)
	username = models.CharField(max_length = 30)
	points = 0
	"""I'm debating whether points should be initialized as an int or as a string and converted into an
	int later. Let me know what you guys think."""
	position = models.CharField(max_length = 30)
	organization = models.CharField(max_length = 60)
	#permissions = {add_points=true}
	#to be added later after determining which types of users have which permissions

	def __str__(self):
		return self.first_name  + " " + self.last_name

	def getUsername(self):
		return self.username

	def getPoints(self):
		return self.points

	def getPosition(self):
		return self.organization

class Event(models.Model):
	name = models.CharField(max_length = 60)
	date = models.CharField(max_length = 30)
	time_hour = models.CharField(max_length = 2)
	time_minute = models.CharField(max_length = 2)
	place = models.CharField(max_length = 40)
	points = 0
	"""I'm debating whether points should be initialized as an int or as a string and converted into an
	int later. Let me know what you guys think."""

	def __str__(self):
		return self.name

	def getDate(self):
		return self.date

	def getTime(self):
		return time_hour + " : " + time_minute

	def getPlace(self):
		return self.place

	def getPoints(self):
		return self.points
