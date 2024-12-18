from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)  
    content = models.TextField(blank=True)
    author_username = models.CharField(max_length=50, default='')  # Armazena o username diretamente
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class PostImage(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='images/posts/', blank=True, null=True)

    def __str__(self):
        return self.post.title