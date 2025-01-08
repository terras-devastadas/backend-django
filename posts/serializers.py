from rest_framework import serializers
from .models import Post, PostImage

class PostImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImage
        fields = ['id', 'image']

class PostSerializer(serializers.ModelSerializer):
    images = PostImageSerializer(many=True, read_only=True)
    image_files = serializers.ListField(
        child=serializers.ImageField(write_only=True),
        write_only=True,
        required=False  # Torna o campo opcional
    )

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'author_username', 'created_at', 'updated_at', 'images', 'image_files']
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