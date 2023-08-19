import requests

LON =78.962883
LAT =20.593683
parameters = {
    "lat": LAT,
    "lng": LON,
    "formatted":0
}
response = requests.get(url="https://api.sunrise-sunset.org/json",params=parameters)
response.raise_for_status()
data = response.json()
Sunrise=data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset=data["results"]["sunset"].split("T")[1].split(":")[0]

print(Sunrise)
