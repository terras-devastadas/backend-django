
from .models import Post
from .serializers import PostSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    # def get_queryset(self):
    #     community_id = self.request.query_params.get('community', None)
    #     if community_id:
    #         return Post.objects.filter(community__id=community_id)
    #     return 
    Post.objects.all()

