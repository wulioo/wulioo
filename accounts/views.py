from django.contrib.auth.hashers import make_password
from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from accounts.models import User
from accounts.serializers import RegisterSerializer


class RegisterViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

    def perform_create(self,serializer):
        serializer.validated_data['password'] = make_password(serializer.initial_data.get('password'))
        serializer.save()


class LoginViewSet(APIView):
    pass