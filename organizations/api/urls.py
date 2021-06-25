from django.urls import path

from .views import OrganizationListCreateView, OrganizationDetailView

urlpatterns = [
    path("organizations/", OrganizationListCreateView.as_view()),
    path('organizations/<int:pk>/', OrganizationDetailView.as_view())
]