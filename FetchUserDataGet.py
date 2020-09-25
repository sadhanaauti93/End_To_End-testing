import requests
import json
import jsonpath
# API URL
url = "https://reqres.in/api/users?page=2"

# Send Get Request
response = requests.get(url)
#print(response)

#  Display Response Content
#print(response.content)
#print(response.headers)
# Parse responce to json formate
json_response = json.loads(response.text)
#print(json_response)

# Fetch value using json path
pages = jsonpath.jsonpath(json_response,'total_pages')
assert pages[0] == 2
