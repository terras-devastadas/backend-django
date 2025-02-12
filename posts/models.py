from django.db import models
from community.models import Community
from customUser.models import CustomUser


class Post(models.Model):
    title = models.CharField(max_length=100)  
    content = models.TextField(blank=True)
   
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='images/posts/', blank=True, default='')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='posts')
    community = models.CharField(max_length=100, default='')

    
    def __str__(self):
        return self.title
