from django.urls import reverse
from rest_framework import status
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework.test import APITestCase
from django.contrib.auth.models import User



class UserImageTest(APITestCase):
    pass


class EndpointsTestCase(APITestCase):

    def setUp(self):  
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.access_token = AccessToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + str(self.access_token))

    def test_get_routes(self):
        url = reverse('get-routes')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_routes(self):
        url = reverse('get-routes')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_upload_image(self):
        url = reverse('upload-image')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)