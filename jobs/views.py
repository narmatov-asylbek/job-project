from django.urls import reverse_lazy, reverse
from django.http import Http404, HttpResponseRedirect
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import JobForm
from .models import Job
from organizations.models import Organization


class HomePageView(ListView):
    model = Job
    template_name = 'homepage.html'
    paginate_by = 7

    def get_queryset(self):
        return Job.objects.filter(is_approved=True)


class JobCreateView(LoginRequiredMixin, CreateView):
    model = Job
    form_class = JobForm
    template_name = 'jobs/job_create_form.html'
    success_url = reverse_lazy('jobs:job-detail')

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('jobs:job-detail', args=[self.object.pk])


class JobDetailView(DetailView):
    model = Job
    template_name = 'jobs/job_detail.html'
    context_object_name = 'job'

    def get_context_data(self, **kwargs):
        context = super(JobDetailView, self).get_context_data(**kwargs)
        job = self.get_object()
        organization = Organization.objects.get(id=job.organization.id)
        context['organization'] = organization
        return context


class JobUpdateView(LoginRequiredMixin, UpdateView):
    model = Job
    form_class = JobForm
    template_name = 'jobs/job_update.html'
    success_url = reverse_lazy('user-detail')

    def dispatch(self, request, *args, **kwargs):
        if self.get_object().creator != request.user:
            raise Http404
        return super(JobUpdateView, self).dispatch(self.request, *args, **kwargs)


class JobDeleteView(LoginRequiredMixin, DeleteView):
    model = Job
    success_url = reverse_lazy('user-detail')

    def dispatch(self, request, *args, **kwargs):
        if self.get_object().creator != request.user:
            raise Http404
        return super(JobDeleteView, self).dispatch(self.request, *args, **kwargs)


class JobListView(ListView):
    model = Job
    template_name = 'jobs/job_list.html'
    context_object_name = 'jobs'
    paginate_by = 10

    def get_queryset(self):
        return Job.objects.filter(is_approved=True)
