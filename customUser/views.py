from rest_framework import viewsets
from .models import CustomUser
from .serializers import CustomUserSerializer

from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from rest_framework import status
import logging
from rest_framework.authtoken.views import obtain_auth_token, Token

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
        token, created = Token.objects.get_or_create(user=user)
        try:
            send_mail(
                'Confirmação de Cadastro',
                f'Obrigado por se cadastrar, {name} \n\n http://localhost:5173/{token}',
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=False
                
            )
            logger.debug("Email de confirmação enviado para %s", email)
        except Exception as e:
            logger.error("Erro ao enviar email para %s: %s", email, e)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

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
        serializer = CustomUserSerializer(user)
        return Response(serializer.data)
    
    def post(self, request):
        user = request.user
        serializer = CustomUserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    