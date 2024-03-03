from django.urls import path
from . import views

urlpatterns = [
    path('get-routes/', views.get_routes),
]