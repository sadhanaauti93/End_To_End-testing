import requests
import json
import jsonpath

#API URL
url = "https://reqres.in/api/users/2"

# Read Input Json File
file = open('F:\\CreateUser.Json', 'r')
json_input = file.read()
request_json = json.loads(json_input)

# Make Put request  with json input body
response = requests.put(url, request_json)

# validating response code
assert response.status_code == 200

# Parse response to json formate
response_json = json.loads(response.text)
updated_li = jsonpath.jsonpath(response_json, 'updatedAt')
print(updated_li)
