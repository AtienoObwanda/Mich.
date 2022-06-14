import statistics
from  rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework import status
from django.db.models import Avg
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import AuthenticationFailed
import jwt, datetime
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny

from django.shortcuts import redirect, get_object_or_404



from .models import *
from .serializer import ProjectSerializer

from users.models import Profile

  # TESTING PROJECT ON POSTMAN
class TestProjectApi(APIView):
    permission_classes = (IsAuthenticated,)
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
    permission_classes = (AllowAny,)


    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'projects/project_list.html'

    def get(self, request, format=None):
        # profile = Profile.objects.get(profile_pk=pk)
        projects = Project.objects.all()
        return Response({'projects':projects})


class ProjectDetailList(APIView):
    permission_classes = [IsAuthenticated]
    renderer_classes= [TemplateHTMLRenderer]
    template_name='projects/project_detail.html'


    def get(self, request, pk):
        
       
        projectUsability = Review.objects.filter(project_id=pk).aggregate(Avg('usability'))
        projectContent = Review.objects.filter(project_id=pk).aggregate(Avg('content'))
        projectDesign = Review.objects.filter(project_id=pk).aggregate(Avg('design'))
        reviews = Review.objects.filter(project_id=pk)
        project = get_object_or_404(Project, pk=pk)

        '''
        Calculating the average rating score
        '''
        # content = [score.content for score in reviews]
        # contentAverage = sum(content) / len(content)

        # design = [score.design for score in reviews]
        # designAverage = sum(design) / len(design)

        # usability = [score.usability for score in reviews]
        # usabilityAverage = sum(usability) / len(usability)   
        
        # scoreAv= (contentAverage + designAverage + usabilityAverage) / 3
        
        # scoreAverage = str(round(scoreAv, 2))
        return Response({'project': project, 'reviews':reviews, 'projectUsability': projectUsability, 'projectDesign':projectDesign, 'projectContent': projectContent})
