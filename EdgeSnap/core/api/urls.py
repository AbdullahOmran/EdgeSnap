from django.urls import path
from . import views

from rest_framework_simplejwt.views import TokenRefreshView
from .views import MyTokenObtainPairView

urlpatterns = [
    path('get-routes/', views.get_routes, name = 'get-routes'),
    path('token/', MyTokenObtainPairView.as_view(), name='token-obtain-pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('upload-image/', views.upload_image, name = 'upload-image'),
    path('get-grayscale/', views.get_grayscale , name = 'get-grayscale'),
    path('add-gaussian-noise/', views.add_gaussian_noise, name = 'add-gaussian-noise'),
    path('add-uniform-noise/', views.add_uniform_noise, name = 'add-uniform-noise'),
    path('add-salt-and-pepper-noise/', views.add_salt_and_pepper_noise,  name = 'add-salt-and-pepper-noise'),
    path('blur/', views.blur, name = 'blur'),
    path('gaussian-blur/', views.gaussian_blur, name = 'gaussian-blur'),
]
