import requests

endpoints = 'http://127.0.0.1:8000/info/'

get_response = requests.get(url= endpoints)
data = get_response.json()
print(data)