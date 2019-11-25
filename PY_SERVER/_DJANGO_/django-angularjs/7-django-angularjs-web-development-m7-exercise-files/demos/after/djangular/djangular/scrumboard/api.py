from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions

from .models import List, Card
from .serializers import ListSerializer, CardSerializer, ProjectSerializer


class ListViewSet(ModelViewSet):
    queryset = List.objects.all()
    serializer_class = ListSerializer
    permission_classes = (permissions.IsAuthenticated,)


class CardViewSet(ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    permission_classes = (permissions.IsAuthenticated,)


class ProjectViewSet(ModelViewSet):
    def get_queryset(self):
        user = self.request.user
        return user.projects.all()

    serializer_class = ProjectSerializer
    permission_classes = (permissions.IsAuthenticated,)
