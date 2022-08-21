from django.db import models
from django.contrib.auth.models import User


class Competitions(models.Model):
    competition_name = models.CharField(max_length=50, blank=False, unique=True)
    location = models.CharField(max_length=50, blank=False)
    club_name = models.CharField(max_length=50, blank=False, unique=True)


    def __str__(self):
        return self.competition_name
