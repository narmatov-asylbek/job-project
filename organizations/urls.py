from django.urls import path

from .views import OrganizationListView, OrganizationCreateView, OrganizationDetailView

app_name = 'organizations'
urlpatterns = [
    path('<int:pk>/', OrganizationDetailView.as_view(), name='organization-detail'),
    path('new/', OrganizationCreateView.as_view(), name='organization-create'),
    path('', OrganizationListView.as_view(), name='organization-list'),
]