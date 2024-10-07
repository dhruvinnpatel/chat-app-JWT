from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework.response import Response
from .models import UserData

class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
         

class UserListView(APIView):
    def get(self, request):
        users = UserData.objects.all() 
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data) 