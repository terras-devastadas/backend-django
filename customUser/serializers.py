from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
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
        user = super().create(validated_data)
        if password:
            user.set_password(password)
            user.save()
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)
        if password:
            user.set_password(password)
            user.save()
        return user