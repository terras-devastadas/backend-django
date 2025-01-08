from rest_framework import viewsets
from .models import Community
from .serializers import CommunitySerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
class CommunityViewset(viewsets.ModelViewSet):
    queryset = Community.objects.all()
    serializer_class = CommunitySerializer
    # permission_classes = [IsAuthenticated]

    #Acesso só através da comunidade pai
    @action(detail=True, methods=['get'])
    def subcommunities(self, request, pk=None):
        community = get_object_or_404(Community, pk=pk)
        subcommunities = community.subcommunities.filter(is_subcommunity=True)
        serializer = CommunitySerializer(subcommunities, many=True)
        return Response(serializer.data)