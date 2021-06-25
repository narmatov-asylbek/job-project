from jobs.models import Job

from rest_framework import serializers


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = (
            'id',
            'organization',
            'job_position',
            'description',
            'type',
            'salary',
            'salary_min',
            'salary_max',
            'currency',
            'city',
            'is_expired',
            'created_at',
            'telegram',
            'email',
            'phone'
        )
