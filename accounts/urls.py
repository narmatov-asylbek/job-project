from django.urls import path
from django.contrib.auth import views as auth_views
from .views import UserDetailView

urlpatterns = [
    path('accounts/login/', auth_views.LoginView.as_view(template_name='accounts/login_form.html'), name='login'),
    path('me/', UserDetailView.as_view(), name='user-detail')
]