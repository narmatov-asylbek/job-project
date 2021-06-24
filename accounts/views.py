from django.shortcuts import redirect, render
from django.contrib.auth import logout, login
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, CreateView, RedirectView, FormView

from jobs.models import Job
from .forms import UserRegistrationForm, UserLoginForm
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


class UserLoginView(FormView):
    form_class = UserLoginForm
    template_name = 'accounts/login_form.html'
    success_url = '/'
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(UserLoginView, self).dispatch(self.request, *args, **kwargs)

    def get_success_url(self):
        if "next" in self.request.GET and self.request.GET['next'] != "":
            return self.request.GET['next']
        else:
            return self.success_url

    def form_valid(self, form):
        login(self.request, form.get_user())
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))


class UserLogoutView(RedirectView):
    url = "/"

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(UserLogoutView, self).get(request, *args, **kwargs)


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
