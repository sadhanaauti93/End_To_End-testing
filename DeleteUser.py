import requests

#API URL
url = "https://reqres.in/api/users/2"

respone = requests.delete(url)

# Fetch respone code
print(respone.status_code)

assert respone.status_code == 204