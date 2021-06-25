from rest_framework import permissions
from rest_framework import authentication
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import filters

from organizations.models import Organization
from .serializers import OrganizationSerializer
from jobs.api.permissions import IsCreatorOrReadOnly


class OrganizationListView(ListCreateAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    authentication_classes = [authentication.SessionAuthentication]

    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['name', 'id']
    ordering = ['name']
    search_fields = ['name']

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class OrganizationDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    permission_classes = [IsCreatorOrReadOnly, permissions.IsAuthenticatedOrReadOnly]
    authentication_classes = [authentication.SessionAuthentication]