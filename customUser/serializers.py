from rest_framework import serializers
from .models import CustomUser
import six, uuid, base64
from django.core.files.base import ContentFile   
    
class Base64ImageField(serializers.ImageField):
    def to_internal_value(self, data):
        if data:            
            if isinstance(data, six.string_types) and data.startswith('data:image'):
                format, imgstr = data.split(';base64,')
                ext = format.split('/')[-1]
                unique_name = str(uuid.uuid4())[:12]
                data = ContentFile(base64.b64decode(imgstr), name=f"{unique_name}.{ext}")
            return super().to_internal_value(data)
class CustomUserSerializer(serializers.ModelSerializer):
    photo_profile = Base64ImageField(required=False, allow_null=True)
  
    class Meta:
        model = CustomUser
        fields = '__all__'
        extra_kwargs = { # Campos não enviados para o endpoint
            'password': {'write_only': True},
            'user_permissions': {'write_only': True}
        }



    # Validação de um campo específico
    def validate_email(self, value):
        allowed_domain = 'aluno.unb.br'
        domain = value.split('@')[1]
        if domain != allowed_domain:
            raise serializers.ValidationError('Utilize o email da UnB.')
        return value
    
    
    

    def create(self, validated_data):
        password = validated_data.pop('password', None)        
        email = validated_data.get('email', '')
        matricula = email.split('@')[0]
        validated_data['matricula'] = matricula
        user = super().create(validated_data)
        if password:
            user.set_password(password)
            user.save()
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        email = validated_data.get('email', instance.email)
        matricula = email.split('@')[0]
        validated_data['matricula'] = matricula
        
        user = super().update(instance, validated_data)
        if password:
            user.set_password(password)
            user.save()
        return user
