from typing import List

from rest_framework.views import APIView
from rest_framework.response import Response


class HelloAPIView(APIView):
    """Test API view"""

    def get(self, request, format_=None):
        """Returns a list of APIView features"""
        apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'is similar to a traditional django view',
            'gives you the most controls over your application'
        ]
        return Response({'message': 'Hello!', 'apiview': apiview})

class DefaultAPIView(APIView):
    """APIView if nothing else is provided"""

    def get(self, request, format_=None):
        """Returns a basic cheering message"""
        return Response({'Message': 'Great job, me!'})
