import requests
import json 

endpoints = 'http://127.0.0.1:8000/create/'

data ={
    'name' : 'Rossy',
    'age' : 30,
    'address' : 'Btw',
    'qualification' : 'phd'
}

# Converting above python data into json using json dump
json_data = json.dumps(data)
#Sending the post request
post_request = requests.post(url= endpoints, data=json_data)
data = post_request.json()
print(data)