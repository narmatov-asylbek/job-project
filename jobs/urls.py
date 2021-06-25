from django.urls import path

from .views import JobCreateView, JobDetailView, JobListView, JobUpdateView, JobDeleteView, HomePageView

app_name = 'jobs'
urlpatterns = [
    path('jobs/<int:pk>/update/', JobUpdateView.as_view(), name='job-update'),
    path('jobs/<int:pk>/delete/', JobDeleteView.as_view(), name='job-delete'),
    path('jobs/<int:pk>/', JobDetailView.as_view(), name='job-detail'),
    path('jobs/new/', JobCreateView.as_view(), name='job-create'),
    path('jobs/', JobListView.as_view(), name='job-list'),
    path('', HomePageView.as_view(), name='homepage'),

]