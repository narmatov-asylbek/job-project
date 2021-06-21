from django.shortcuts import render
from django.views.generic import DetailView

from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin

from jobs.models import Job
User = get_user_model()


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'accounts/account-detail.html'
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        context = super(UserDetailView, self).get_context_data(**kwargs)
        context['jobs'] = Job.objects.filter(creator=self.request.user)
        return context

    def get_object(self, queryset=None):
        return self.request.user
