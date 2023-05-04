import requests
import json 

outlines = 'http://127.0.0.1:8000/student_api/'

#reading the data from API
def get_data(id = None):
    data = {}
    if id is not None:
        data = {'id':id}
    json_data = json.dumps(data)
    get_request = requests.get(url= outlines , data= json_data)
    data = get_request.json()
    print(data)    
    
# get_data()

#creating a data
def post_data():
    data = {
        'name': 'Monica',
        'age': 26,
        'address': 'NY',
        'qualification': 'Chef'
    }
    json_data = json.dumps(data)
    post_response = requests.post(url= outlines, data= json_data)
    print(post_response.json())
    
    
# post_data()

#updating the data in API
def update_data():
    data = {
        'id':6, 
        'qualification': 'Chef' #here key is the label in view
    }
    json_data = json.dumps(data)
    request = requests.put(url= outlines, data=json_data)
    print(request.json())

# update_data()

#Deleting the data 
def delete_data():
    data ={ 'id': 2}
    json_data = json.dumps(data)
    request = requests.delete(url = outlines,data=json_data)
    print(request.json())
    
# delete_data()