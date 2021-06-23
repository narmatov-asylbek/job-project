from django.urls import path
from .views import UserDetailView, UserRegistrationView, LogoutView
from django.contrib.auth import views as auth_views


app_name = 'accounts'
urlpatterns = [
    path('sign-up/', UserRegistrationView.as_view(), name='registration'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login_form.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('me/', UserDetailView.as_view(), name='user-detail')
]
