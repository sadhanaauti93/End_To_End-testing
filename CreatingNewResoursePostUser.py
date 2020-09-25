import requests
import json
import jsonpath

#API URL
url = "https://reqres.in/api/users"

# Read Input Json File
file = open('F:\\CreatUser.Json','r')
json_input = file.read()
request_json = json.loads(json_input)

#print(request_json)

# Make Post request  with json input body

response = requests.post(url,json_input)
print(response.content)

# validating response code
assert response.status_code == 201

# Fetch Header from response
print(response.headers.get('content-Length'))

# Parse response to json formate
response_json = json.loads(response.text)

#Pick ID using json path
id = jsonpath.jsonpath(response_json,'id')
print(id[0])