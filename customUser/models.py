from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    lastName = models.CharField(max_length=30)
    firstName = models.CharField(max_length=30)
    bio = models.TextField(blank=True, default='')
    photo_profile = models.ImageField(upload_to='images/profile_pics/', blank=True, null=True)