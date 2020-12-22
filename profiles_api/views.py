from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions


class HelloAPIView(APIView):
    """Test API view"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format_=None):
        """Returns a list of APIView features"""
        apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'is similar to a traditional django view',
            'gives you the most controls over your application'
        ]
        return Response({'message': 'Hello!', 'apiview': apiview})

    def post(self, request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """Update an object"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Partially update an object"""
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'method': 'DELETE'})


class DefaultAPIView(APIView):
    """APIView if nothing else is provided"""

    def get(self, request, format_=None):
        """Returns a basic cheering message"""
        return Response({'Message': 'Great job, me!'})


class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return a hello message"""

        viewset = [
            'Uses actions (list, create, update, delete, partial_update)',
            'Automatically maps to URLs using routes',
            'Provides more functionality with less code'
        ]
        return Response({'message': 'Hello!', 'ViewSet': viewset})

    def create(self, request):
        """Create a new hello message"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """Get a specific object by its id"""
        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """Update an object"""
        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Update part of an object"""
        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Destroy an object"""
        return Response({'http_method': 'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Create and update profile"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)


class UserLoginApiView(ObtainAuthToken):
    """Create user auth tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
