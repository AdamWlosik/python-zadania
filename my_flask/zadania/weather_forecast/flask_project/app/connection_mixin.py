import requests


class ConnectionMixin:
    def __init__(self, url, api_key):
        self.url = url
        self.api_key = api_key

    def get_weather_data(self, location):
        params = {"key": self.api_key, "q": location}
        response = requests.get(self.url, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            return None
