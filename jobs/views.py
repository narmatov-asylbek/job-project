from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import JobCreateForm
from .models import Job
from organizations.models import Organization


class JobCreateView(LoginRequiredMixin, CreateView):
    model = Job
    form_class = JobCreateForm
    template_name = 'jobs/job_create_form.html'
    success_url = reverse_lazy('jobs:job-detail')

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)


class JobDetailView(DetailView):
    model = Job
    template_name = 'jobs/job_detail.html'
    context_object_name = 'job'

    def get_context_data(self, **kwargs):
        context = super(JobDetailView, self).get_context_data(**kwargs)
        job = self.get_object()
        organization = Organization.objects.get(id=job.organization.id, name=job.organization.name)
        context['organization'] = organization
        return context


class JobListView(ListView):
    model = Job
    template_name = 'jobs/job_list.html'
    context_object_name = 'jobs'
    paginate_by = 10

    def get_queryset(self):
        return Job.objects.filter(is_approved=True)