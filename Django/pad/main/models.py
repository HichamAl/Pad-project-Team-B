from django.db import models
from django.contrib.auth.models import User

# Objects and class for the challenges.
class Challenge(models.Model):
    name = models.CharField(max_length=100)
    flag = models.CharField(max_length=100)
    points = models.IntegerField()

# Objects and class of the point system.
class UserPoints(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    points = models.IntegerField(default=0)
    challenges = models.ForeignKey(Challenge, on_delete=models.CASCADE)

    def total_points(self):
        return sum(challenge.points for challenge in self.challenges.all())


# SQL INJECTION SECRET USER 
class SecretUser(models.Model):
    secret_username = models.CharField(max_length=100)
    secret_password = models.CharField(max_length=100)

