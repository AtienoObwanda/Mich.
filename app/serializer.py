from dataclasses import field
from rest_framework import serializers

from .models import *

class ProjectSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Project
        fields = ('projectName', "projectImage", 'projectLink', 'projectDescription','projectCategory', 'projectTechnology', 'projectOwner', 'uploadDate')
    
    def create(self, validated_data):
        instance = self.Meta.model(**validated_data)
        instance.save()
        return instance
