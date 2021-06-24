from django.urls import path
from .views import UserDetailView, UserRegistrationView, UserLogoutView, UserLoginView


app_name = 'accounts'
urlpatterns = [
    path('sign-up/', UserRegistrationView.as_view(), name='registration'),
    path('login/', UserLoginView.as_view(template_name='accounts/login_form.html'), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('me/', UserDetailView.as_view(), name='user-detail')
]
