from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'author_username', 'created_at', 'updated_at', 'image']
        extra_kwargs = {
            'author_username': {'read_only': True},
        }

    def create(self, validated_data):
        image_files = validated_data.pop('image_files', None)  # Pega o campo, se existir
        user = self.context['request'].user
        post = Post.objects.create(author_username=user.username, **validated_data)
        if image_files:
            for image_file in image_files:
                PostImage.objects.create(post=post, image=image_file)
        return post