from django.shortcuts import redirect, render
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, CreateView, RedirectView

from jobs.models import Job
from .forms import UserRegistrationForm
from .models import User


class UserRegistrationView(CreateView):
    model = User
    template_name = 'accounts/registration.html'
    form_class = UserRegistrationForm
    success_url = "/"

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return HttpResponseRedirect('/')
        return super().dispatch(self.request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data.get('password1')
            user.set_password(password)
            user.save()
            return redirect('accounts:login')
        else:
            return render(request, self.template_name, {'form': form})


class LogoutView(RedirectView):
    url = "/"

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)


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
