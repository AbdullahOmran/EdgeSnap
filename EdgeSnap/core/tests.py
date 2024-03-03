
# Create your tests here.
import requests

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


