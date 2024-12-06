from django.db import models

class Community(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    banner = models.ImageField(upload_to='images/banners/', null=True, blank=True)
    visibility_students = models.BooleanField(default=True)
    visibility_teachers= models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
