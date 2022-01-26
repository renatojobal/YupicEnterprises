

# Rest_framework imports
from rest_framework import serializers


# Local imports
from core.models import Project


class ProjectSerializer(serializers.ModelSerializer):
    """
    Serializer for the Project model
    """
    class Meta:
        model = Project
        fields = '__all__'