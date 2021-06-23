from django.views.generic import ListView, CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse

from .models import Organization
from .forms import OrganizationForm
from jobs.models import Job


class OrganizationListView(ListView):
    model = Organization
    template_name = 'organizations/organization_list.html'
    context_object_name = 'organizations'
    paginate_by = 10


class OrganizationDetailView(DetailView):
    model = Organization
    template_name = 'organizations/organization_detail.html'
    context_object_name = 'organization'

    def get_context_data(self, **kwargs):
        organization = self.get_object()
        context = super(OrganizationDetailView, self).get_context_data(**kwargs)
        context['jobs'] = Job.objects.filter(organization=organization, is_approved=True)
        return context


class OrganizationCreateView(LoginRequiredMixin, CreateView):
    model = Organization
    template_name = 'organizations/organization_form.html'
    form_class = OrganizationForm

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super(OrganizationCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('organizations:organization-detail', args=[self.object.pk])