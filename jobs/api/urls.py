from django.urls import path

from .views import JobDetailView, JobsListCreateView

urlpatterns = [
    path('jobs/', JobsListCreateView.as_view()),
    path('jobs/<int:pk>/', JobDetailView.as_view())
]