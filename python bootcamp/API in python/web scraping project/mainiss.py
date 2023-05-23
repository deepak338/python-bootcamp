import requests

response=requests.get(url="http://api.open-notify.org/iss-now.json")

# raise exception error from http not giving exception by ourself

data=response.json()
print(data)