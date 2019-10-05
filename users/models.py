from django.db import models

# Create your models here.


"""This acts as an abstract class to contain common data"""
class User(models.Model):
	first_name = models.CharField(max_length=50, default='')
	last_name = models.CharField(max_length=50, default='')
	joined = models.DateTimeField(auto_now_add=True)
	team = models.CharField(max_length=100,default='')
	class Meta:
		abstract = True
		ordering = ['joined']

class Admin(User):

class Staff(User):
	department = models.CharField(max_length=50,default='')
	points = models.IntegerField(max_length=10,blank=True,default=0)
	mon_raised = models.IntegerField(max_length=20,blank=True,default=0)

class Dancer(User):
	points = models.IntegerField(max_length=10,blank=True,default=0)
	mon_raised = models.IntegerField(max_length=20, blank=True,default=0)

class Guest(User):
	first_name = models.CharField(null=True)
	last_name = models.CharField(null=True)
	joined = models.DateField(null=True)
	team = models.CharField(null=True)

