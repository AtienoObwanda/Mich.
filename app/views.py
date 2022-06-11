from django.shortcuts import render
from  rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializer import ProjectSerializer

class ProjectList(APIView):
    def get(self, request, format=None):
        allProjects = Project.objects.all()
        serializers = ProjectSerializer(allProjects, many=True)
        return Response(serializers.data)
