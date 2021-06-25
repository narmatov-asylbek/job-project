from django.urls import path

from .views import JobDetailView, JobListView, ApiRootView

urlpatterns = [
    path('', ApiRootView.as_view(), name='api-root'),
    path('jobs/', JobListView.as_view(), name='api-job-list'),
    path('jobs/<int:pk>/', JobDetailView.as_view())
]