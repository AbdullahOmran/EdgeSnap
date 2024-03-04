from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import MyTokenObtainPairSerializer
from django.http import HttpResponse
from ..models import UserImage
from rest_framework import status
import cv2 as cv
import numpy as np
import os

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_routes(request):
    routes = [
        '/api/get-routes/',
        '/api/',
    ]
    return Response(routes)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def upload_img(request):
    images = UserImage.objects.filter(user=request.user)
    if images.count() > 0:
        for image in images:
            image.delete()
    instance = UserImage(user=request.user, image=request.FILES['image'], out_image = request.FILES['image'])
    instance.save()
    return Response(status.HTTP_201_CREATED)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_grayscale(request):
    try:
        user_image = UserImage.objects.get(user = request.user)
        filename = str(user_image.image)
        out_file = str(user_image.out_image)
        img = cv.imread(filename)
        gray_image = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        cv.imwrite(out_file, gray_image)
        user_image.save()
        with open(out_file, 'rb') as f:
            extension = os.path.splitext(filename)[1] 
            return HttpResponse(f, content_type='image/'+ extension[1:])
    except UserImage.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)

    return Response(status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def add_noise(request):
    pass

