import requests
import os
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/weather"  # end point
app_key = 'b35d5b022bffa533d164e188fc9292af'
account_sid = os.environ['ACa2c4bc8caea033bca9035b03c892dabd']
auth_token = os.environ['d770153925326a261819e71ce17139f6']
weather_parameter = {
    "lat": 22.572645,
    "lon": 88.363892,
    "appid": app_key,
    "exculde": "current,daily",
}

reponse = requests.get(OWM_Endpoint, params=weather_parameter)
reponse.raise_for_status()
weather_data = reponse.json()
weather_condition = (weather_data["weather"][0]['id'])
print(weather_condition)

if int(weather_condition) < 700:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="you should get your umbrella ,it going to rain, have a  day(if you did not forget to get your umbralle)",
        from_='+15017122661',
        to='+918340667756'
    )
    print(message.status)
