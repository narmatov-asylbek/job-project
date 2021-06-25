from django.urls import path

from .views import OrganizationListView, OrganizationDetailView

urlpatterns = [
    path("organizations/", OrganizationListView.as_view(), name='api-organization-list'),
    path('organizations/<int:pk>/', OrganizationDetailView.as_view())
]