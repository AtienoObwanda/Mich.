from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response    
from rest_framework.exceptions import AuthenticationFailed
import jwt, datetime

from .serializers import *


class RegisterUser(APIView):
    def post(self,request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


