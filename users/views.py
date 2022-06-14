from re import A
from django.shortcuts import redirect, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response    
from rest_framework.exceptions import AuthenticationFailed
import jwt, datetime
from rest_framework.renderers import TemplateHTMLRenderer
# from django.http import HttpResponseRedirect
from rest_framework.parsers import FormParser, MultiPartParser, JSONParser
from django.contrib.auth import login
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics


from .serializers import *

from app.models import *
from app.serializer import ProjectSerializer,ReviewSerializer


class RegisterUser(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'register_user.html'
    model = User
    def get(self, request):
        serializer = UserSerializer()
        return Response({'serializer': serializer})

    def post(self,request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        # return Response(serializer.data)
        return redirect('login')

class LoginUser(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'login_user.html'
    model = User
    def get(self, request):
        serializer = LoginSerializer()
        # serializer = UserSerializer()
        return Response({'serializer': serializer})

    def post (self,request):
        email = request.data['email']
        password = request.data['password']

        user = User.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed('User not found')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password')

        
        payload={
            'id' : user.id,
            'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat' : datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256') 
        
        response = Response()

        response.set_cookie(key = 'jwt' , value = token, httponly = True)

        response.data = {
            'jwt' : token
        }

        return redirect ('projects')


class ProfileView(APIView):
    
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'profile_view.html'

    def get(self, request):
        token = request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed('Invalid Session!')

        try:
            payload = jwt.decode(token, 'secret', algorithms = ['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Session expired!')
            
        user = User.objects.filter(id=payload['id']).first()
        serializer = UserSerializer(user)
        return Response(serializer.data)


class LogoutView(APIView):
   
    def post(self, request):
        response = Response()
        response.delete_cookie(jwt)
        
        response.data = {
            'message' : 'success'
        }
        return redirect('login')





# project related views


class AddProject(APIView):
    permission_classes = [IsAuthenticated]

    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'projects/add_project.html'
    parser_classes = [JSONParser,FormParser,MultiPartParser]

    model = Project
    def get(self, request):
        serializer = ProjectSerializer()
        return Response({'serializer': serializer})

    def post(self, request, format=None):
        # project = get_object_or_404(Project, pk=pk)
        serializer = ProjectSerializer(data = request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer})
        serializer.save()

        return redirect('projects') # Configure to return the auther profile

class UpdatePoject(APIView):
    permission_classes = [IsAuthenticated]
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'projects/update_project.html'

    def get(self, request, pk):
        project = get_object_or_404(Project, pk=pk)
        serializer = ProjectSerializer(project)
        return Response({'serializer': serializer, 'project': project})

    def put(self, request, pk):
        project = get_object_or_404(Project, pk=pk)
        serializer = ProjectSerializer(project, data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'project': project})
        serializer.save()
        return redirect('projectDetail',pk)


class DeleteProject(APIView):
    permission_classes = [IsAuthenticated]
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'projects/delete_project.html'

    def get(self, request, pk):
        project = get_object_or_404(Project, pk=pk)
        serializer = ProjectSerializer(project)
        return Response({'serializer': serializer, 'project': project})
    
    def delete(self, request, pk):
        profile = get_object_or_404(Project, pk=pk)
        profile.delete()
        return redirect('projects') #  Configure to return the auther profile




class UserProfile(APIView):
    permission_classes = [IsAuthenticated]
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'users/user_profile.html'
    parser_classes = [JSONParser,FormParser,MultiPartParser]

    model = Profile
    def get(self, request,pk):
        profile = Profile.objects.get(pk=pk)
        # user = get_object_or_404(User, pk=pk)
        user = profile.user
        projects = Project.objects.filter(projectOwner=user).order_by('-uploadDate')
        serializer = ProfileSerializer()
        return Response({'serializer': serializer, 'profile':profile, 'user':user, 'projects':projects})





class EditProfile(APIView):

    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'users/update_profile.html'
    parser_classes = [JSONParser,FormParser,MultiPartParser]

    model = Profile
    def get(self, request,pk):
        profile = Profile.objects.get(pk=pk)
        # user = get_object_or_404(User, pk=pk)
        user = profile.user
        projects = Project.objects.filter(projectOwner=user).order_by('-uploadDate')
        serializer = ProfileSerializer()
        return Response({'serializer': serializer, 'profile':profile, 'user':user, 'projects':projects})

    def post(self, request, pk,format=None):
        profile = Profile.objects.get(pk=pk)
        serializer = ProfileSerializer(data = request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer})
        serializer.save()

        return redirect('profile',pk) # Configure to return the auther profile

class AddReview(APIView):

    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'projects/add_review.html'
    parser_classes = [JSONParser,FormParser,MultiPartParser]

    model = Review
    def get(self, request, pk):
        project = get_object_or_404(Project, pk=pk)
        serializer = ReviewSerializer()
        return Response({'serializer': serializer, 'project': project})

    def post(self, request,pk):
        project = get_object_or_404(Project, pk=pk)
        serializer = ReviewSerializer(data = request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer})
        serializer.save()
        # return HttpResponseRedirect('projectDetail') # Configure to return the author profile
        return redirect('projectDetail',pk)





















