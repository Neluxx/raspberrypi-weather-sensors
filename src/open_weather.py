#!/usr/bin/env python3
"""
Open Weather Map
"""

import os
import requests


class OpenWeather:
    """Open Weather Class"""

    def __init__(self):
        self.api_key = os.getenv("API_KEY")
        self.city_name = os.getenv("CITY_NAME")

    def get_data(self):
        """Get response from open weather map"""

        base_url = "https://api.openweathermap.org/data/2.5/weather"
        params = {"q": self.city_name, "appid": self.api_key, "units": "metric"}

        try:
            response = requests.get(base_url, params=params)
            data = response.json()

            if response.status_code == 200:
                return data

            else:
                print("Fehler beim Abrufen der Daten. Statuscode:", response.status_code)
                return None

        except requests.RequestException as exception:
            print("Fehler bei der Anfrage:", exception)
            return None
