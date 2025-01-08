from django.db import models

class Community(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    banner = models.ImageField(upload_to='images/banners/', null=True, blank=True)
    visibility_students = models.BooleanField(default=True)
    visibility_teachers= models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='subcommunities', on_delete=models.SET_NULL)
    is_subcommunity = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.parent:
            self.is_subcommunity = True
        else:
            self.is_subcommunity = False
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
