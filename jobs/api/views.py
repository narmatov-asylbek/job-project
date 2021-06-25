from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import permissions
from rest_framework import authentication

from .serializers import JobSerializer
from jobs.models import Job
from .permissions import IsCreatorOrReadOnly


class JobsListCreateView(ListCreateAPIView):
    serializer_class = JobSerializer
    queryset = Job.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    authentication_classes = [authentication.SessionAuthentication]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class JobDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = JobSerializer
    queryset = Job.objects.all()
    permission_classes = [IsCreatorOrReadOnly, permissions.IsAuthenticatedOrReadOnly]