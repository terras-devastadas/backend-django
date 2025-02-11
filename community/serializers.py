from rest_framework import serializers
from .models import Community

import base64
from django.core.files.base import ContentFile     
import uuid
import six

class Base64ImageField(serializers.ImageField):
    def to_internal_value(self, data):
        if data:   
            if isinstance(data, six.string_types) and data.startswith('data:image'):
                format, imgstr = data.split(';base64,')
                ext = format.split('/')[-1]
                unique_name = str(uuid.uuid4())[:12]
                data = ContentFile(base64.b64decode(imgstr), name=f"{unique_name}.{ext}")
            return super().to_internal_value(data)
class CommunitySerializer(serializers.ModelSerializer):
    subcommunities = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    banner = Base64ImageField(required=False, allow_null=True)
    class Meta:
        model = Community
        fields = '__all__'
        
