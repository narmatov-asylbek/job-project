from django.urls import path

from .views import UserListView, UserRetrieveUpdateDestroyView, registration

urlpatterns = [
    path('users/', UserListView.as_view(), name='api-user-list'),
    path('users/<int:pk>/', UserRetrieveUpdateDestroyView.as_view()),
    path('registration/', registration),
]