import requests, json
from django.conf import settings

API_KEY = settings.API_KEY

BASE_URL = "http://api.weatherapi.com/v1/"


class Location:
    """
    Location of forecast area
    """

    def __init__(self, city="", postal=""):
        if postal:
            self.q = postal
        else:
            self.q = city

    def _forecastResponse(self):
        return requests.get(
            BASE_URL + "forecast.json",
            params={
                "key": API_KEY,
                "q": self.q,
                "days": 7,
                "alerts": "yes",
                "aqi": "yes",
            },
        )

    def getForecast(self):
        """
        Returns JSON of forecast, False if error.
        """
        response = self._forecastResponse()
        if response.status_code == 200:
            return response.json()
        else:
            return False
