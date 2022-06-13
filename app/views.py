from  rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework import status
from django.db.models import Avg

from django.shortcuts import redirect, get_object_or_404



from .models import *
from .serializer import ProjectSerializer


  # TESTING PROJECT ON POSTMAN
class TestProjectApi(APIView):

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





class AllProjectList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'projects/project_list.html'

    def get(self, request, format=None):
        projects = Project.objects.all()
        return Response({'projects':projects})


class ProjectDetailList(APIView):
    renderer_classes= [TemplateHTMLRenderer]
    template_name='projects/project_detail.html'


    def get(self, request, pk):
        usability = Review.objects.filter(project_id=pk).aggregate(Avg('usability'))
        content = Review.objects.filter(project_id=pk).aggregate(Avg('content'))
        design = Review.objects.filter(project_id=pk).aggregate(Avg('design'))
        reviews = Review.objects.filter(project_id=pk)
        project = get_object_or_404(Project, pk=pk)
        return Response({'project': project, 'reviews':reviews, 'usability': usability, 'design':design, 'content': content})
