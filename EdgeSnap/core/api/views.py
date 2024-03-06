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
from . import utils
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
def upload_image(request):
    images = UserImage.objects.filter(user=request.user)
    if images.count() > 0:
        for image in images:
            image.delete()
    instance = UserImage(user=request.user, image=request.FILES['image'], out_image = request.FILES['image'])
    instance.save()
    return Response(status = status.HTTP_201_CREATED)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_grayscale(request):
    try:
        user_image = UserImage.objects.get(user = request.user)
        
        filename = str(user_image.out_image)
        img = cv.imread(filename)
        gray_image = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        cv.imwrite(filename, gray_image)
        user_image.save()
        with open(filename, 'rb') as f:
            extension = os.path.splitext(filename)[1] 
            return HttpResponse(f, content_type='image/'+ extension[1:])
    except UserImage.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    return Response(status = status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def add_gaussian_noise(request):
    mean = request.GET.get('mean',None)
    std = request.GET.get('std',None)
    if std is None or mean is None:
        return Response(status = status.HTTP_400_BAD_REQUEST)
    mean = float(mean)
    std = float(std)
    try:
        user_image = UserImage.objects.get(user = request.user)
        
        filename = str(user_image.out_image)
        img = cv.imread(filename)
        gray_image  = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        row,col = gray_image.shape
        noise = np.random.normal(mean,std, (row,col))
        noisy_image = gray_image + noise
        noisy_image = np.clip(noisy_image,0,255).astype(np.uint8)
        cv.imwrite(filename, noisy_image)
        user_image.save()
        with open(filename, 'rb') as f:
            extension = os.path.splitext(filename)[1] 
            return HttpResponse(f, content_type='image/'+ extension[1:])
    except UserImage.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    return Response(status = status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def add_uniform_noise(request):
    low = request.GET.get('low',None)
    high = request.GET.get('high',None)
    if low is None or high is None:
        return Response(status = status.HTTP_400_BAD_REQUEST)
    low = float(low)
    high = float(high)
    try:
        user_image = UserImage.objects.get(user = request.user)
        
        filename = str(user_image.out_image)
        img = cv.imread(filename)
        gray_image  = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        row,col = gray_image.shape
        noise = np.random.uniform(low,high, (row,col))
        noisy_image = gray_image + noise
        noisy_image = np.clip(noisy_image,0,255).astype(np.uint8)
        cv.imwrite(filename, noisy_image)
        user_image.save()
        with open(filename, 'rb') as f:
            extension = os.path.splitext(filename)[1] 
            return HttpResponse(f, content_type='image/'+ extension[1:])
    except UserImage.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    return Response(status = status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def add_salt_and_pepper_noise(request):
    saltiness = request.GET.get('saltiness',None)
    pepperiness = request.GET.get('pepperiness',None)
    if saltiness is None and pepperiness is None:
        return Response(status = status.HTTP_400_BAD_REQUEST)
    try:
        user_image = UserImage.objects.get(user = request.user)
        
        filename = str(user_image.out_image)
        img = cv.imread(filename)
        gray_image  = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        noisy_image = np.copy(gray_image)
        width,height = gray_image.shape
        if saltiness is not None:
            saltiness = float(saltiness)
            num_salt = np.floor(gray_image.size * saltiness)
            salt_x_vector = np.random.randint(0,width, int(num_salt))
            salt_y_vector = np.random.randint(0,height, int(num_salt))
            noisy_image[salt_x_vector, salt_y_vector] = 255
        if pepperiness is not None:
            pepperiness = float(pepperiness)
            num_pepper = np.floor(gray_image.size * pepperiness)
            pepper_x_vector = np.random.randint(0,width, int(num_pepper))
            pepper_y_vector = np.random.randint(0,height, int(num_pepper))
            noisy_image[pepper_x_vector, pepper_y_vector] = 0

        cv.imwrite(filename, noisy_image)
        user_image.save()
        with open(filename, 'rb') as f:
            extension = os.path.splitext(filename)[1] 
            return HttpResponse(f, content_type='image/'+ extension[1:])
    except UserImage.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def blur(request):
    kernel_size = request.GET.get('kernel',None)
    if kernel_size is None:
        return Response(status = status.HTTP_400_BAD_REQUEST)
    kernel_size = int(kernel_size)
    try:
        user_image = UserImage.objects.get(user = request.user)
        
        filename = str(user_image.out_image)
        img = cv.imread(filename)
        gray_image  = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        row,col = gray_image.shape
        kernel = np.ones(shape = (kernel_size, kernel_size) ) / (kernel_size**2)
        filtered_image = cv.filter2D(src = gray_image,kernel=kernel,anchor=(-1,-1), ddepth = -1)
        cv.imwrite(filename, filtered_image)
        user_image.save()
        with open(filename, 'rb') as f:
            extension = os.path.splitext(filename)[1] 
            return HttpResponse(f, content_type='image/'+ extension[1:])
    except UserImage.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    return Response(status = status.HTTP_200_OK)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def gaussian_blur(request):
    kernel_size = request.GET.get('kernel',None)
    std = request.GET.get('std',None)
    if kernel_size is None or std is None:
        return Response(status = status.HTTP_400_BAD_REQUEST)
    kernel_size = int(kernel_size)
    std = float(std)
    try:
        user_image = UserImage.objects.get(user = request.user)
        
        filename = str(user_image.out_image)
        img = cv.imread(filename)
        gray_image  = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        row,col = gray_image.shape
        kernel = utils.gaussian_kernel(kernel_size, std)
        filtered_image = cv.filter2D(src = gray_image,kernel=kernel,anchor=(-1,-1), ddepth = -1)
        cv.imwrite(filename, filtered_image)
        user_image.save()
        with open(filename, 'rb') as f:
            extension = os.path.splitext(filename)[1] 
            return HttpResponse(f, content_type='image/'+ extension[1:])
    except UserImage.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    return Response(status = status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def median_blur(request):
    kernel_size = request.GET.get('kernel',None)
    if kernel_size is None:
        return Response(status = status.HTTP_400_BAD_REQUEST)
    kernel_size = int(kernel_size)
    try:
        user_image = UserImage.objects.get(user = request.user)
        
        filename = str(user_image.out_image)
        img = cv.imread(filename)
        gray_image  = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        filtered_image = utils.apply_median_blur(gray_image, kernel_size)
        cv.imwrite(filename, filtered_image)
        user_image.save()
        with open(filename, 'rb') as f:
            extension = os.path.splitext(filename)[1] 
            return HttpResponse(f, content_type='image/'+ extension[1:])
    except UserImage.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    return Response(status = status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def sobel_edge_detection(request):
    
    try:
        user_image = UserImage.objects.get(user = request.user)
        filename = str(user_image.out_image)
        img = cv.imread(filename)
        gray_image  = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        edited_image = utils.apply_sobel_edge_detection(gray_image)
        cv.imwrite(filename, edited_image)
        user_image.save()
        with open(filename, 'rb') as f:
            extension = os.path.splitext(filename)[1] 
            return HttpResponse(f, content_type='image/'+ extension[1:])
    except UserImage.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    return Response(status = status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def roberts_edge_detection(request):
    
    try:
        user_image = UserImage.objects.get(user = request.user)
        filename = str(user_image.out_image)
        img = cv.imread(filename)
        gray_image  = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        edited_image = utils.apply_roberts_edge_detection(gray_image)
        cv.imwrite(filename, edited_image)
        user_image.save()
        with open(filename, 'rb') as f:
            extension = os.path.splitext(filename)[1] 
            return HttpResponse(f, content_type='image/'+ extension[1:])
    except UserImage.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    return Response(status = status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def prewitt_edge_detection(request):
    
    try:
        user_image = UserImage.objects.get(user = request.user)
        filename = str(user_image.out_image)
        img = cv.imread(filename)
        gray_image  = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        edited_image = utils.apply_prewitt_edge_detection(gray_image)
        cv.imwrite(filename, edited_image)
        user_image.save()
        with open(filename, 'rb') as f:
            extension = os.path.splitext(filename)[1] 
            return HttpResponse(f, content_type='image/'+ extension[1:])
    except UserImage.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    return Response(status = status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def canny_edge_detection(request):
    low_threshold = request.GET.get('low_threshold',None)
    high_threshold = request.GET.get('high_threshold',None)
    if low_threshold is None or high_threshold is None:
        return Response(status = status.HTTP_400_BAD_REQUEST)
    low_threshold = int(low_threshold)
    high_threshold = int(high_threshold)
    try:
        user_image = UserImage.objects.get(user = request.user)
        filename = str(user_image.out_image)
        img = cv.imread(filename)
        gray_image  = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        edited_image = cv.Canny(gray_image, low_threshold, high_threshold)
        cv.imwrite(filename, edited_image)
        user_image.save()
        with open(filename, 'rb') as f:
            extension = os.path.splitext(filename)[1] 
            return HttpResponse(f, content_type='image/'+ extension[1:])
    except UserImage.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    return Response(status = status.HTTP_200_OK)


