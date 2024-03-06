
# Create your tests here.
import requests
import cv2 as cv
import numpy as np

class TestAPIClient(object):
    
    def __init__(self):
        self.BASE_URL = 'http://localhost:8000/api'

        self.endpoints = {
            'token':f'{self.BASE_URL}/token/',
            'get-routes':f'{self.BASE_URL}/get-routes/',
            'upload-image':f'{self.BASE_URL}/upload-image/',
            'get-grayscale':f'{self.BASE_URL}/get-grayscale/',
            'add-gaussian-noise':f'{self.BASE_URL}/add-gaussian-noise/',
            'add-uniform-noise':f'{self.BASE_URL}/api/add-uniform-noise/',
            'add-salt-and-pepper-noise':f'{self.BASE_URL}/add-salt-and-pepper-noise/',
            'blur':f'{self.BASE_URL}/blur/',
        }
        res = requests.post(self.reverse('token'), data={
            'username': 'AbdullahOmran',
            'password': '123456789',
        })
        access_token = None
        if res.status_code == 200:
           access_token = res.json().get('access')

        self.headers = {
            'Authorization': 'Bearer '+ access_token
        }

        self.files = {
            'image': open(r"G:\my-projects\centrifuge-web-app\public\images\drug_img.jpg",'rb')
        }

        res = requests.post(self.reverse('upload-image'), files=self.files, headers=self.headers)

    def reverse(self,endpoint):
        return self.endpoints.get(endpoint)

    def test_get_grayscale(self):
        res = requests.get(self.reverse('get-grayscale'), headers=self.headers)

        index = res.headers.get('Content-Type').find('/')+1
        out_file = 'output.'+res.headers.get('Content-Type')[index:]

        img_bytes = np.frombuffer(res.content, dtype=np.uint8)
        image =cv.imdecode(img_bytes, cv.IMREAD_COLOR)
        cv.imshow(out_file,image)
        cv.waitKey(0)
        cv.destroyAllWindows()

    def test_add_gaussian_noise(self,mean=1, std=50):
        payload = {
            'mean': mean,
            'std': std,
        }
        res = requests.get(self.reverse('add-gaussian-noise'),params=payload, headers=self.headers)

        index = res.headers.get('Content-Type').find('/')+1
        out_file = 'output.'+res.headers.get('Content-Type')[index:]
        img_bytes = np.frombuffer(res.content, dtype=np.uint8)
        image =cv.imdecode(img_bytes, cv.IMREAD_COLOR)
        cv.imshow(out_file,image)
        cv.waitKey(0)
        cv.destroyAllWindows()

    def test_add_uniform_noise(self, low = 0, high = 50):
        payload = {
            'low': low,
            'high': high
        }
        res = requests.get(self.reverse('add-uniform-noise'),params=payload, headers=self.headers)

        index = res.headers.get('Content-Type').find('/')+1
        out_file = 'output.'+res.headers.get('Content-Type')[index:]
        img_bytes = np.frombuffer(res.content, dtype=np.uint8)
        image =cv.imdecode(img_bytes, cv.IMREAD_COLOR)
        cv.imshow(out_file,image)
        cv.waitKey(0)
        cv.destroyAllWindows()

    def test_add_salt_and_pepper_noise(self, saltiness = 0.5, pepperiness = 0.5):
        payload = {
            'saltiness': saltiness,
            'pepperiness': pepperiness
        }
        res = requests.get(self.reverse('add-salt-and-pepper-noise'),params=payload, headers=self.headers)

        index = res.headers.get('Content-Type').find('/')+1
        out_file = 'output.'+res.headers.get('Content-Type')[index:]
        img_bytes = np.frombuffer(res.content, dtype=np.uint8)
        image =cv.imdecode(img_bytes, cv.IMREAD_COLOR)
        cv.imshow(out_file,image)
        cv.waitKey(0)
        cv.destroyAllWindows()

    def test_blur(self, kernel_size = 3):
        payload = {
            'kernel': kernel_size,

        }
        res = requests.get(self.reverse('blur'),params=payload, headers=self.headers)

        index = res.headers.get('Content-Type').find('/')+1
        out_file = 'output.'+res.headers.get('Content-Type')[index:]
        img_bytes = np.frombuffer(res.content, dtype=np.uint8)
        image =cv.imdecode(img_bytes, cv.IMREAD_COLOR)
        cv.imshow(out_file,image)
        cv.waitKey(0)
        cv.destroyAllWindows()




