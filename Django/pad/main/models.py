from django.db import models
from django.contrib.auth.models import User

class Challenge(models.Model):
    name = models.CharField(max_length=100)
    flag = models.CharField(max_length=100)
    points = models.IntegerField()

class UserPoints(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    points = models.IntegerField(default=0)
    challenges = models.ForeignKey(Challenge, on_delete=models.CASCADE)

    def total_points(self):
        return sum(challenge.points for challenge in self.challenges.all())


