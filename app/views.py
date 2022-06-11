from django.shortcuts import render, get_object_or_404
from  rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework import status
from django.http import HttpResponseRedirect



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
        project = get_object_or_404(Project, pk=pk)
        return Response({'project': project})

class AddProject(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'add_project.html'
    model = Project
    def get(self, request):
        serializer = ProjectSerializer()
        return Response({'serializer': serializer})

    def post(self, request):
        # project = get_object_or_404(Project, pk=pk)
        serializer = ProjectSerializer( data = request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer})
        serializer.save()

        return HttpResponseRedirect('') # Configure to return the auther profile

class UpdatePoject(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'projects/update_project.html'

    def get(self, request, pk):
        project = get_object_or_404(Project, pk=pk)
        serializer = ProjectSerializer(project)
        return Response({'serializer': serializer, 'project': project})

    def put(self, request, pk):
        profile = get_object_or_404(Project, pk=pk)
        serializer = ProjectSerializer(profile, data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'profile': profile})
        serializer.save()
        return HttpResponseRedirect('project')


class DeleteProject(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'projects/delete_project.html'

    def get(self, request, pk):
        project = get_object_or_404(Project, pk=pk)
        serializer = ProjectSerializer(project)
        return Response({'serializer': serializer, 'project': project})
    
    def delete(self, request, pk):
        profile = get_object_or_404(Project, pk=pk)
        profile.delete()
        return HttpResponseRedirect('') #  Configure to return the auther profile
