from django.urls import path

from .views import JobCreateView, JobDetailView, JobListView, JobUpdateView

app_name = 'jobs'
urlpatterns = [
    path('<int:pk>/update/', JobUpdateView.as_view(), name='job-update'),
    path('<int:pk>/', JobDetailView.as_view(), name='job-detail'),
    path('new/', JobCreateView.as_view(), name='job-create'),
    path('', JobListView.as_view(), name='job-list')

]