from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class RunningSession(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=2000)
    location = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return "%s" % (self.title)
