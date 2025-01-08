from rest_framework import serializers
from .models import Community

class CommunitySerializer(serializers.ModelSerializer):
    subcommunities = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Community
        fields = ['id', 'name', 'description', 'banner', 'visibility_students', 'visibility_teachers', 'created_at', 'parent', 'subcommunities']