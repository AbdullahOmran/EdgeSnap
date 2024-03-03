
# Create your tests here.
import requests

res = requests.post('http://localhost:8000/api/get-routes/')

print(res.text)