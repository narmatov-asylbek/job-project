from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import permissions
from rest_framework import authentication
from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import JobSerializer
from jobs.models import Job
from .permissions import IsCreatorOrReadOnly


class ApiRootView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):
        return Response({
            'user-list': reverse('api-user-list', request=request),
            'organization-list': reverse('api-organization-list', request=request),
            'job-list': reverse('api-job-list', request=request)
        })


class JobListView(ListCreateAPIView):
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