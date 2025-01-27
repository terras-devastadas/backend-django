from django.shortcuts import render
from .models import Post
from .serializers import PostSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
import base64
import io
from PIL import Image
from rest_framework.response import Response

class PostViewSet(viewsets.ModelViewSet):
    permmision_classes = [IsAuthenticated]
    

    
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    def perform_create(self, serializer):
        serializer.save(author_username=self.request.user)

    # def get_queryset(self):
    #     community_id = self.request.query_params.get('community', None)
    #     if community_id:
    #         return Post.objects.filter(community__id=community_id)
    #     return 
    Post.objects.all()

