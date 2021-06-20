from django.urls import path

from .views import JobCreateView, JobDetailView, JobListView

app_name = 'jobs'
urlpatterns = [
    path('new/', JobCreateView.as_view(), name='job-create'),
    path('<int:pk>', JobDetailView.as_view(), name='job-detail'),
    path('', JobListView.as_view(), name='job-list')

]