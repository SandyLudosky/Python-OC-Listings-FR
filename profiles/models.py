from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """Profile model for Profiles app
    Args:
        models.Model (class): The base class for Django models.
    Attributes:
        user (User): The user associated with this profile.
        favorite_city (str): The user's favorite city.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        return self.user.username
