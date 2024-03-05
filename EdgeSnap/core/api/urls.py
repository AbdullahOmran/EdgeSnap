from django.urls import path
from . import views

from rest_framework_simplejwt.views import TokenRefreshView
from .views import MyTokenObtainPairView

urlpatterns = [
    path('get-routes/', views.get_routes),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('upload-image/', views.upload_img),
    path('get-grayscale/', views.get_grayscale),
    path('add-gaussian-noise/', views.add_gaussian_noise),
    path('add-uniform-noise/', views.add_uniform_noise),
    path('add-salt-and-pepper-noise/', views.add_salt_and_pepper_noise),
    path('blur/', views.blur),
]
