from django.db import models
from django.utils import timezone

class Event(models.Model):
    name = models.CharField(max_length = 60)
    time = models.DateTimeField(default=timezone.now)
    place = models.CharField(max_length = 180)
    code = models.CharField(max_length = 20, blank=True)
    points = models.IntegerField(default = 0)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ('time',)

    def __str__(self):
        return self.name
