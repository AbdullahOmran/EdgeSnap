from rest_framework.response import Response
from rest_framework.decorators import api_view
import cv2 as cv




@api_view(['GET'])
def get_routes(request):
    routes = [
        '/api/get-routes/',
        '/api/',
    ]
    return Response(routes)


@api_view(['POST'])
def add_noise(request):
    pass

@api_view(['POST'])
def get_grayscale(request):
    img = cv.imread(request.data)
