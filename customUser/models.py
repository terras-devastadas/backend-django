from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):

    bio = models.TextField(blank=True, default='')
    photo_profile = models.ImageField(upload_to='images/profile_pics/', blank=True, null=True)
    matricula = models.CharField(max_length=8, blank=True)