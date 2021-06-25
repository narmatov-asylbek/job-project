from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import permissions
from rest_framework import authentication
from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import filters

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
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]

    ordering_fields = ['job_position', 'created_at', 'is_expired', 'salary_min']
    ordering = ['job_position']
    search_fields = ['job_position']


    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class JobDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = JobSerializer
    queryset = Job.objects.all()
    permission_classes = [IsCreatorOrReadOnly, permissions.IsAuthenticatedOrReadOnly]