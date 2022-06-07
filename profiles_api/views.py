from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API view"""

    def get(self, response, format=None):
        """ Returns a  list of APIView features"""

        an_apiview = [
            'Uses HTTP methods as functions (get, post, put, patch, delete)',
            'It is similar to a traditional Django view',
            'Gives you the most control over your application logic',
            'It is mapped to urls manually',
        ]

        return Response({'message': 'Hello', 'an_apiview': an_apiview})
