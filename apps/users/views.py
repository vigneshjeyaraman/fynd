from rest_framework.mixins import (ListModelMixin, CreateModelMixin,
                                   UpdateModelMixin, DestroyModelMixin)

from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import viewsets, permissions
from apps.users.serializers import (UserSignupSerializer, UserSerializer,
                                        LoginSerializer)
from apps.movies.models import (Movies)

class Signup(CreateModelMixin, viewsets.GenericViewSet):
    """Class to handle user signup"""
    def create(self, request):
        data = request.data
        serializer = UserSignupSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        user_obj = serializer.save()
        serializer = UserSerializer(user_obj)
        token = Token.objects.create(user=user_obj)
        data = serializer.data
        data.update({"token":token.key})
        return Response(data=data, status=200)

class Login(CreateModelMixin, viewsets.GenericViewSet):
    """View to login user and return their token"""
    def create(self, request):
        data = request.data
        serializer = LoginSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        token, _ = Token.objects.get_or_create(user=serializer.validated_data.get('user'))
        serializer = UserSerializer(serializer.validated_data.get('user'))
        data = serializer.data
        data.update({"token":token.key})
        return Response(data=data, status=200)
