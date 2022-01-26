# Django imports
from django.shortcuts import render

# Rest_framework imports
from rest_framework.viewsets import ModelViewSet


# Local imports
from core.models import Project

from core.serializers import ProjectSerializer



class ProjectViewset(ModelViewSet):
    """
    API endpoint that allows projects to be viewed or edited.
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer