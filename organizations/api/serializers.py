from rest_framework import serializers

from organizations.models import Organization

from jobs.api.serializers import JobSerializer


class OrganizationSerializer(serializers.ModelSerializer):
    jobs = JobSerializer(read_only=True, many=True)

    class Meta:
        model = Organization
        fields = (
            'id',
            'logo',
            'name',
            'description',
            'website',
            'jobs'
        )
