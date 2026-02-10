from rest_framework.response import Response
from rest_framework.decorators import api_view
# Defined home page here


@api_view(['GET'])
def home_page(request):
    return Response({"message": "Welcome to Fashion Website"})
