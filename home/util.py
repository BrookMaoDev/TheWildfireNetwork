import requests
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

    def is_valid(self):
        if self._forecastResponse().status_code == 200:
            return True
        return False

    def _forecastResponse(self):
        return requests.get(
            BASE_URL + "current.json",
            params={
                "key": API_KEY,
                "q": self.q,
            },
        )

    def getForecast(self):
        """
        Returns dict of forecast, None if error.
        """
        response = self._forecastResponse()
        if response.status_code == 200:
            return response.json()
        else:
            return {}

    def calculateFireRisk(self, temp_c, humidity, wind_kph):
        """
        0: Low fire risk
        1: Moderate fire risk
        2: High fire risk
        3+: Extreme fire risk
        """

        # Define threshold values for each factor (30 30 30 rule)
        tempThreshold = 30  # Celsius
        humidityThreshold = 30  # Percentage
        windThreshold = 30  # km/h

        # Calculate fire risk based on factors' relation to thresholds
        fireRisk = 0
        message = ""

        if temp_c >= tempThreshold:
            fireRisk += 1
            message += "The temperature is high enough to pose a risk of fire. Higher temperature reduce moisture content in the air and can create more intense fires that spread faster.\n"

        if humidity <= humidityThreshold:
            fireRisk += 1
            message += "The humidity is low enough to pose a risk of fire. Drier air leads to reduced moisture and faster evaporation, which both increase fire spread and intensity.\n"

        if wind_kph >= windThreshold:
            fireRisk += 1
            message += "The wind speed is high enough to greatly increase the risk of any fires. High wind speeds can cause fires to spread more rapidly, carrying flames and embers while supplying them with oxygen.\n"

        if fireRisk == 0:
            message += "\nThere is a low fire risk in your area."
        elif fireRisk == 1:
            message += "\nThere is a moderate fire risk in your area."
        elif fireRisk == 2:
            message += "\nThere is a high fire risk in your area."
        else:
            message += "\nThere is an extreme fire risk in your area."

        return message
