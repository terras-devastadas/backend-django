
from .models import Post
from .serializers import PostSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

class PostViewSet(viewsets.ModelViewSet):
    permmision_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)  # Salve o autor como o usuário autenticado

    def get_queryset(self):
        queryset = Post.objects.all()
        community = self.request.query_params.get('community', None)
        if community is not None:
            return Post.objects.filter(community=community)
        return queryset
    

