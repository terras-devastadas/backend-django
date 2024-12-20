from rest_framework import serializers
from .models import Community

class CommunitySerializer(serializers.ModelSerializer):
    subcommunities = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Community
        fields = ['id', 'name', 'description', 'banner', 'visibility', 'created_at', 'parent', 'subcommunities', 'is_subcommunity'] 