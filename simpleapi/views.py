from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework import viewsets

# Create your views here.

class UserAccessAllSet(viewsets.ModelViewSet):
    permission_classes = (IsAdminUser,)
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer
    
    
class UserReadSet(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        permission_classes = (IsAuthenticated,)
        submenu = User.objects.all().filter(username=request.user)
        serializer = UserSerializer(submenu, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)