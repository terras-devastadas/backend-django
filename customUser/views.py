from rest_framework import viewsets
from .models import CustomUser
from .serializers import CustomUserSerializer
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from rest_framework import status
import logging
from rest_framework.authtoken.models import Token
from django.template.loader import render_to_string
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated


logger = logging.getLogger(__name__)

class CustomUserViewset(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    lookup_field = 'email'

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        
        user = serializer.instance  # Recupera o objeto criado diretamente do serializer
        
        name = user.username
        email = user.email
        
        # gera link de confirmação
        token, created = Token.objects.get_or_create(user=user)
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        activation_link = f"{settings.BACKEND_URL}/activate/{uid}/{token.key}/"
        
        try:
            send_mail(
                'Confirmação de Cadastro',
                f'Obrigado por se cadastrar, {name} \n\n Clique no link para ativar sua conta: {activation_link}',
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=False
            )
            logger.debug("Email de confirmação enviado para %s", email)
        except Exception as e:
            logger.error("Erro ao enviar email para %s: %s", email, e)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
class ActivateAccount(APIView):
    def get(self, request, uidb64, token):
        try:
            uid = urlsafe_base64_decode(uidb64).decode()
            user = CustomUser.objects.get(pk=uid)
        except Exception as e:
            logger.error("Erro ao ativar conta: %s", e)
            return HttpResponse("Link inválido.")
        
        if Token.objects.filter(user=user, key=token).exists():
            user.is_active = True
            user.save()
            return HttpResponse("Conta ativada com sucesso.")
        return HttpResponse("Link inválido.")

class LogoutView(APIView):
    """
    Logout básico usando exclusão do token do DRF.
    """
    permission_classes = [IsAuthenticated]

    def post(self, request):
        request.auth.delete()
        return Response({"message": "Logout realizado com sucesso."})
    
class InfoUserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response({
            'username': user.username,
            'email': user.email,
            'firstName': user.firstName,
            'lastName': user.lastName,
            #is_staff acesso a administração pode ser usado para indicar se é professor
            'is_staff': user.is_staff,
            # 'is_superuser': user.is_superuser,
            'is_active': user.is_active,
            'date_joined': user.date_joined,
            'last_login': user.last_login,
            'photo_profile': user.photo_profile.url,
        })
         
    