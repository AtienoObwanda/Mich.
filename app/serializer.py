from dataclasses import field, fields
from pyexpat import model
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


class AddProjectSerializer(serializers.Serializer):
    class Meta:
        model = Project
        fields = "__all__"
    
    def create(self, validated_data):
        instance = self.Meta.model(**validated_data)
        instance.save()
        return instance



class CommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comment
        fields = "__all__"

    def create(self, validated_data):
        instance = self.Meta.model(**validated_data)
        instance.save()
        return instance

class ReviewSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Review
        fields = "__all__"

    def create(self, validated_data):
        instance = self.Meta.model(**validated_data)
        instance.save()
        return instance


