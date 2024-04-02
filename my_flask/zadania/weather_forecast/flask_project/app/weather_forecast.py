import os.path

from .connection_mixin import ConnectionMixin
from .file_mixin import FileMixin


class WeatherForecast(FileMixin, ConnectionMixin):
    def __init__(self, file_name, url, api_key):
        FileMixin.__init__(self, file_name)
        ConnectionMixin.__init__(self, url, api_key)
        self.data = {}

    def fetch_weather_forecast(self, location, date_time):
        if os.path.exists(self.file_name):
            # Sprawdź, czy plik istnieje
            cached_data = self.read_data()
            if cached_data:
                # Sprawdź, czy dla danej lokalizacji i daty mamy już dane pogodowe w pliku
                if location in cached_data and date_time in cached_data[location]:
                    self.data = cached_data
                else:
                    # Dane dla danej lokalizacji i daty nie istnieją w pliku, pobierz dane z API
                    weather_data = self.get_weather_data(location)
                    if weather_data:
                        # Zapisz nowe dane do pliku
                        if location not in cached_data:
                            cached_data[location] = {}
                        cached_data[location][date_time] = {
                            "timestamp": date_time,
                            "weather": weather_data["current"],
                        }
                        self.write_data(cached_data)

                        # Wczytaj nowe dane
                        self.data = cached_data
                    else:
                        print("Failed to fetch weather data")
            else:
                print("File is empty")
        else:
            # Plik nie istnieje, pobierz dane z API i zapisz do pliku
            weather_data = self.get_weather_data(location)
            if weather_data:
                self.data = {"timestamp": date_time, "weather": weather_data["current"]}
                self.write_data({location: {date_time: self.data}})
            else:
                print("Failed to fetch weather data")

    def display_weather_forecast(self, location, date_time):
        # print(self.data)

        data = self.data[location][date_time]
        # print(data)
        # print("Weather forecast for", location, "at", data['timestamp'])
        # print("Temperature:", data['weather']['temp_c'], "°C")
        # print("Humidity:", data['weather']['humidity'], "%")
        # print("Cloud:", data['weather']['cloud'], "%")
        # print("Wind speed:", data['weather']['wind_kph'], "km/h")
        # print("Pressure:", data['weather']['pressure_mb'], "mb")
        # print("Chance of rain:", data['weather'].get('chance_of_rain', "N/A"), "%")
        # print("Chance of snow:", data['weather'].get('chance_of_snow', "N/A"), "%")
        return data
