from rest_framework import serializers
from .models import *

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'
        # ('projectName', 'projectImage', 'projectLink', 'projectDescription','projectCategory', 'projectTechnology','projectOwner','uploadDate')

