from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_comunidades, name='listar_comunidades'),
    path('criar/', views.criar_comunidade, name='criar_comunidade'),
    path('atualizar/<int:pk>/', views.atualizar_comunidade, name='atualizar_comunidade'),
    path('deletar/<int:pk>/', views.deletar_comunidade, name='deletar_comunidade'),
]
