
from .models import Post
from .serializers import PostSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
class PostViewSet(viewsets.ModelViewSet):
    permmision_classes = [IsAuthenticated]
    

    
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)  # Salve o autor como o usuário autenticado

    # def get_queryset(self):
    #     community_id = self.request.query_params.get('community', None)
    #     if community_id:
    #         return Post.objects.filter(community__id=community_id)
    #     return 
    

