from email import message
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers


class HelloApiView(APIView):
    """Test API view"""
    serializer_class = serializers.HelloSerializers

    def get(self, response, format=None):
        """ Returns a  list of APIView features"""

        an_apiview = [
            'Uses HTTP methods as functions (get, post, put, patch, delete)',
            'It is similar to a traditional Django view',
            'Gives you the most control over your application logic',
            'It is mapped to urls manually',
        ]

        return Response({'message': 'Hello', 'an_apiview': an_apiview})
    
    def post(self, request):
        """Create Hello message wit our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(serializer.errors, 
            status=status.HTTP_400_BAD_REQUEST
            )
    
    def put(self, request, pk=None):
        """Update an object"""
        return Response({'method':'PUT'})
    
    def patch(self, request, pk=None):
        """Partially update an object"""
        return Response({'method':'PATCH'})
    
    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'method':'DELETE'})