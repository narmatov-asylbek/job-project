from jobs.models import Job

from rest_framework import serializers


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = (
            'creator',
            'organization',
            'job_position',
            'description',
            'type',
        )