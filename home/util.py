import requests, json
from django.conf import settings

API_KEY = settings.API_KEY

BASE_URL = "http://api.weatherapi.com/v1/current.json"

response = requests.get(BASE_URL, params={"key": API_KEY, "q": "Toronto"}).json()
