from django.shortcuts import render
from  rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework import status

from .models import *
from .serializer import ProjectSerializer

class AllProjectList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'projects/project_list.html'

    def get(self, request, format=None):
        projects = Project.objects.all()
        # serializer = ProjectSerializer(projects, many=True)
        # return Response(serializers.data)
        return Response({'projects':projects})

    
class ProjectList(APIView):
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request, format=None):
        projects = Project.objects.all()
        serializers = ProjectSerializer(projects, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = ProjectSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
