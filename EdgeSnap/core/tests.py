
# Create your tests here.
import requests
import cv2 as cv
import numpy as np

res = requests.post('http://localhost:8000/api/token/', data={
    'username': 'AbdullahOmran',
    'password': '123456789',
})
access_token = None
if res.status_code == 200:
   access_token = res.json().get('access')

headers = {
    'Authorization': 'Bearer '+ access_token
}

files = {
    'image': open(r"G:\my-projects\centrifuge-web-app\public\images\drug_img.jpg",'rb')
}

res = requests.post('http://localhost:8000/api/upload-image/', files=files, headers=headers)



def test_get_grayscale():
    res = requests.get('http://localhost:8000/api/get-grayscale/', headers=headers)

    index = res.headers.get('Content-Type').find('/')+1
    out_file = 'output.'+res.headers.get('Content-Type')[index:]

    img_bytes = np.frombuffer(res.content, dtype=np.uint8)
    image =cv.imdecode(img_bytes, cv.IMREAD_COLOR)
    cv.imshow(out_file,image)
    cv.waitKey(0)
    cv.destroyAllWindows()

def test_add_gaussian_noise():
    mean = 1
    std = 50
    payload = {
        'mean': mean,
        'std': std,
    }
    res = requests.get('http://localhost:8000/api/add-gaussian-noise/',params=payload, headers=headers)

    index = res.headers.get('Content-Type').find('/')+1
    out_file = 'output.'+res.headers.get('Content-Type')[index:]
    img_bytes = np.frombuffer(res.content, dtype=np.uint8)
    image =cv.imdecode(img_bytes, cv.IMREAD_COLOR)
    cv.imshow(out_file,image)
    cv.waitKey(0)
    cv.destroyAllWindows()

def test_add_uniform_noise():
    low =0
    high =  50
    payload = {
        'low': low,
        'high': high
    }
    res = requests.get('http://localhost:8000/api/add-uniform-noise/',params=payload, headers=headers)

    index = res.headers.get('Content-Type').find('/')+1
    out_file = 'output.'+res.headers.get('Content-Type')[index:]
    img_bytes = np.frombuffer(res.content, dtype=np.uint8)
    image =cv.imdecode(img_bytes, cv.IMREAD_COLOR)
    cv.imshow(out_file,image)
    cv.waitKey(0)
    cv.destroyAllWindows()

test_add_uniform_noise()

