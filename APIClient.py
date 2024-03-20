
# Create your tests here.
import requests
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt

class APIClient(object):
    
    def __init__(self):
        self.BASE_URL = 'http://localhost:8000/api'

        self.endpoints = {
            'token':f'{self.BASE_URL}/token/',
            'get-routes':f'{self.BASE_URL}/get-routes/',
            'upload-image':f'{self.BASE_URL}/upload-image/',
            'get-grayscale':f'{self.BASE_URL}/get-grayscale/',
            'add-gaussian-noise':f'{self.BASE_URL}/add-gaussian-noise/',
            'add-uniform-noise':f'{self.BASE_URL}/add-uniform-noise/',
            'add-salt-and-pepper-noise':f'{self.BASE_URL}/add-salt-and-pepper-noise/',
            'blur':f'{self.BASE_URL}/blur/',
            'gaussian-blur':f'{self.BASE_URL}/gaussian-blur/',
            'median-blur':f'{self.BASE_URL}/median-blur/',
            'sobel-edge-detection':f'{self.BASE_URL}/sobel-edge-detection/',
            'roberts-edge-detection':f'{self.BASE_URL}/roberts-edge-detection/',
            'prewitt-edge-detection':f'{self.BASE_URL}/prewitt-edge-detection/',
            'canny-edge-detection':f'{self.BASE_URL}/canny-edge-detection/',
            'get-histogram':f'{self.BASE_URL}/get-histogram/',
            'get-equalized-histogram':f'{self.BASE_URL}/get-equalized-histogram/',
            'get-equalized-image':f'{self.BASE_URL}/get-equalized-image/',
            'normalize':f'{self.BASE_URL}/normalize/',
            'global-threshold':f'{self.BASE_URL}/global-threshold/',
            'local-threshold':f'{self.BASE_URL}/local-threshold/',
            'get-hybrid-image':f'{self.BASE_URL}/get-hybrid-image/',
            'get-cdf-distribution':f'{self.BASE_URL}/get-cdf-distribution/',
            
        }

        self.headers = None

    def login(self, username,password):

        res = requests.post(self.reverse('token'), data={
            'username': username,
            'password': password,
        })
        access_token = None
        if res.status_code == 200:
           access_token = res.json().get('access')
        else:
            return False

        self.headers = {
            'Authorization': 'Bearer '+ access_token
        }

        return True

    def upload_image(self,filename):
        self.files = {
            'image': open(filename,'rb')
        }

        res = requests.post(self.reverse('upload-image'), files=self.files, headers=self.headers)

    def reverse(self,endpoint):
        return self.endpoints.get(endpoint)

    def get_grayscale(self):
        res = requests.get(self.reverse('get-grayscale'), headers=self.headers)

        index = res.headers.get('Content-Type').find('/')+1
        out_file = 'output.'+res.headers.get('Content-Type')[index:]

        img_bytes = np.frombuffer(res.content, dtype=np.uint8)
        qimage = QImage.fromData(img_bytes)
        pixmap = QPixmap.fromImage(qimage)
        return pixmap
        

    def add_gaussian_noise(self,mean=1, std=50):
        payload = {
            'mean': mean,
            'std': std,
        }
        res = requests.get(self.reverse('add-gaussian-noise'),params=payload, headers=self.headers)

        index = res.headers.get('Content-Type').find('/')+1
        out_file = 'output.'+res.headers.get('Content-Type')[index:]
        img_bytes = np.frombuffer(res.content, dtype=np.uint8)
        qimage = QImage.fromData(img_bytes)
        pixmap = QPixmap.fromImage(qimage)
        return pixmap

    def add_uniform_noise(self, low = 0, high = 50):
        payload = {
            'low': low,
            'high': high
        }
        res = requests.get(self.reverse('add-uniform-noise'),params=payload, headers=self.headers)

        index = res.headers.get('Content-Type').find('/')+1
        out_file = 'output.'+res.headers.get('Content-Type')[index:]
        img_bytes = np.frombuffer(res.content, dtype=np.uint8)
        qimage = QImage.fromData(img_bytes)
        pixmap = QPixmap.fromImage(qimage)
        return pixmap

    def add_salt_and_pepper_noise(self, saltiness = 0.5, pepperiness = 0.5):
        payload = {
            'saltiness': saltiness,
            'pepperiness': pepperiness
        }
        res = requests.get(self.reverse('add-salt-and-pepper-noise'),params=payload, headers=self.headers)

        index = res.headers.get('Content-Type').find('/')+1
        out_file = 'output.'+res.headers.get('Content-Type')[index:]
        img_bytes = np.frombuffer(res.content, dtype=np.uint8)
        qimage = QImage.fromData(img_bytes)
        pixmap = QPixmap.fromImage(qimage)
        return pixmap

    def blur(self, kernel_size = 3):
        payload = {
            'kernel': kernel_size,

        }
        res = requests.get(self.reverse('blur'),params=payload, headers=self.headers)

        index = res.headers.get('Content-Type').find('/')+1
        out_file = 'output.'+res.headers.get('Content-Type')[index:]
        img_bytes = np.frombuffer(res.content, dtype=np.uint8)
        qimage = QImage.fromData(img_bytes)
        pixmap = QPixmap.fromImage(qimage)
        return pixmap

    def gaussian_blur(self, kernel_size = 3, std = 1):
        payload = {
            'kernel': kernel_size,
            'std':std,
        }
        res = requests.get(self.reverse('gaussian-blur'),params=payload, headers=self.headers)

        index = res.headers.get('Content-Type').find('/')+1
        out_file = 'output.'+res.headers.get('Content-Type')[index:]
        img_bytes = np.frombuffer(res.content, dtype=np.uint8)
        qimage = QImage.fromData(img_bytes)
        pixmap = QPixmap.fromImage(qimage)
        return pixmap

    def median_blur(self, kernel_size = 3):
        payload = {
            'kernel': kernel_size,
        }
        res = requests.get(self.reverse('median-blur'),params=payload, headers=self.headers)

        index = res.headers.get('Content-Type').find('/')+1
        out_file = 'output.'+res.headers.get('Content-Type')[index:]
        img_bytes = np.frombuffer(res.content, dtype=np.uint8)
        qimage = QImage.fromData(img_bytes)
        pixmap = QPixmap.fromImage(qimage)
        return pixmap

    def sobel_edge_detection(self):
        res = requests.get(self.reverse('sobel-edge-detection'), headers=self.headers)
        index = res.headers.get('Content-Type').find('/')+1
        out_file = 'output.'+res.headers.get('Content-Type')[index:]
        img_bytes = np.frombuffer(res.content, dtype=np.uint8)
        qimage = QImage.fromData(img_bytes)
        pixmap = QPixmap.fromImage(qimage)
        return pixmap

    def roberts_edge_detection(self):
        res = requests.get(self.reverse('roberts-edge-detection'), headers=self.headers)
        index = res.headers.get('Content-Type').find('/')+1
        out_file = 'output.'+res.headers.get('Content-Type')[index:]
        img_bytes = np.frombuffer(res.content, dtype=np.uint8)
        qimage = QImage.fromData(img_bytes)
        pixmap = QPixmap.fromImage(qimage)
        return pixmap

    def prewitt_edge_detection(self):
        res = requests.get(self.reverse('prewitt-edge-detection'), headers=self.headers)
        index = res.headers.get('Content-Type').find('/')+1
        out_file = 'output.'+res.headers.get('Content-Type')[index:]
        img_bytes = np.frombuffer(res.content, dtype=np.uint8)
        qimage = QImage.fromData(img_bytes)
        pixmap = QPixmap.fromImage(qimage)
        return pixmap

    def canny_edge_detection(self, low_threshold = 50 , high_threshold = 150):
        payload = {
            'low_threshold': low_threshold,
            'high_threshold': high_threshold,
        }
        res = requests.get(self.reverse('canny-edge-detection'),params=payload, headers=self.headers)
        index = res.headers.get('Content-Type').find('/')+1
        out_file = 'output.'+res.headers.get('Content-Type')[index:]
        img_bytes = np.frombuffer(res.content, dtype=np.uint8)
        qimage = QImage.fromData(img_bytes)
        pixmap = QPixmap.fromImage(qimage)
        return pixmap

    def get_histogram(self, channel = 0, image_type = 'gray'):
        payload = {
            'channel': channel,
            'image_type': image_type,
        }
        res = requests.get(self.reverse('get-histogram'),params=payload, headers=self.headers)
        
        histogram = np.frombuffer(res.content, dtype=np.uint8)
        
        plt.hist(histogram, bins=256, color='blue')
        plt.xlabel('levels')
        plt.ylabel('Frequency')
        plt.title('Basic Histogram')
        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0) 
        image_bytes = buffer.getvalue()
        qimage = QImage.fromData(image_bytes)
        pixmap = QPixmap.fromImage(qimage)
        plt.close()
        return pixmap
        
        

    def get_equalized_histogram(self):
        
        res = requests.get(self.reverse('get-equalized-histogram'), headers=self.headers)
        
        equalized_histogram = np.frombuffer(res.content, dtype=np.uint8)
        plt.hist(equalized_histogram, bins=256, color='blue')
        plt.xlabel('levels')
        plt.ylabel('Frequency')
        plt.title('Equalized Histogram')
        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0) 
        image_bytes = buffer.getvalue()
        qimage = QImage.fromData(image_bytes)
        pixmap = QPixmap.fromImage(qimage)
        plt.close()
        return pixmap
    
    def normalize(self):
        res = requests.get(self.reverse('normalize'), headers=self.headers)
        index = res.headers.get('Content-Type').find('/')+1
        out_file = 'output.'+res.headers.get('Content-Type')[index:]
        img_bytes = np.frombuffer(res.content, dtype=np.uint8)
        image =cv.imdecode(img_bytes, cv.IMREAD_COLOR)
        qimage = QImage.fromData(img_bytes)
        pixmap = QPixmap.fromImage(qimage)
        return pixmap
    
    def global_threshold(self, threshold = 50):
        payload = {
            'threshold': threshold,
        }
        res = requests.get(self.reverse('global-threshold'),params=payload, headers=self.headers)
        index = res.headers.get('Content-Type').find('/')+1
        out_file = 'output.'+res.headers.get('Content-Type')[index:]
        img_bytes = np.frombuffer(res.content, dtype=np.uint8)
        image =cv.imdecode(img_bytes, cv.IMREAD_COLOR)
        qimage = QImage.fromData(img_bytes)
        pixmap = QPixmap.fromImage(qimage)
        return pixmap

    def local_threshold(self, kernel_size = 11):
        payload = {
            'kernel': kernel_size,
        }
        res = requests.get(self.reverse('local-threshold'),params=payload, headers=self.headers)
        index = res.headers.get('Content-Type').find('/')+1
        out_file = 'output.'+res.headers.get('Content-Type')[index:]
        img_bytes = np.frombuffer(res.content, dtype=np.uint8)
        qimage = QImage.fromData(img_bytes)
        pixmap = QPixmap.fromImage(qimage)
        return pixmap

    def get_equalized_image(self):
        
        res = requests.get(self.reverse('get-equalized-image'), headers=self.headers)
        index = res.headers.get('Content-Type').find('/')+1
        out_file = 'output.'+res.headers.get('Content-Type')[index:]
        img_bytes = np.frombuffer(res.content, dtype=np.uint8)
        qimage = QImage.fromData(img_bytes)
        pixmap = QPixmap.fromImage(qimage)
        return pixmap

    def get_hybrid_image(self,filename_1,filename_2,low_pass_cuttoff_freq, high_pass_cuttoff_freq ):
        data = {
            'low_pass_cuttoff_freq':low_pass_cuttoff_freq,
            'high_pass_cuttoff_freq':high_pass_cuttoff_freq
        }
        files = {
            'first_image': open(filename_1,'rb'),
            'second_image': open(filename_2,'rb'),
        }
        res = requests.post(self.reverse('get-hybrid-image'),data=data,files = files, headers=self.headers)
        index = res.headers.get('Content-Type').find('/')+1
        out_file = 'output.'+res.headers.get('Content-Type')[index:]
        img_bytes = np.frombuffer(res.content, dtype=np.uint8)
        qimage = QImage.fromData(img_bytes)
        pixmap = QPixmap.fromImage(qimage)
        return pixmap
    def get_cdf_distribution(self):
        
        res = requests.get(self.reverse('get-cdf-distribution'), headers=self.headers)
        
        cdf_distribution = np.frombuffer(res.content, dtype=np.float32)
        
        plt.plot(cdf_distribution)
        plt.xlabel('levels')
        plt.ylabel('cdf')
        plt.title('Distribution')
        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0) 
        image_bytes = buffer.getvalue()
        qimage = QImage.fromData(image_bytes)
        pixmap = QPixmap.fromImage(qimage)
        plt.close()
        return pixmap




