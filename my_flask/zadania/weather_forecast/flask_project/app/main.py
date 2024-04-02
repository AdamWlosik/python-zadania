import json
import time
from datetime import datetime

from flask import Blueprint, redirect, render_template, request, url_for

from .weather_forecast import WeatherForecast

app_blueprint = Blueprint("app", __name__)
display_forecast_blueprint = Blueprint("display_forecast", __name__)
global location, date_time
file_name = "weather_date.json"
api_url = "https://api.weatherapi.com/v1/current.json"
# TODO link nie chce współpracować działa jeszcze /forecast.json 	nie działa /future.json
api_key = "b99a17a73c824419988144105240204"
weather_forecast = WeatherForecast(file_name, api_url, api_key)


@app_blueprint.route("/", methods=["POST", "GET"])
def app():
    if request.method == "POST":
        global location, date_time
        location = request.form["location"]
        date_time_str = request.form["date_time"]
        date_time_obj = datetime.strptime(date_time_str, "%Y-%m-%dT%H:%M")
        date_time = str(date_time_obj)
        weather_forecast.fetch_weather_forecast(location, date_time)
        json_file_path = (
            r"C:\Users\adamw\OneDrive\Pulpit\Mentoring\python-zadania\my_flask\zadania\weather_forecast"
            r"\flask_project\weather_date.json"
        )
        while True:
            try:
                with open(json_file_path, "r"):
                    pass
            except FileNotFoundError:
                print("Oczekiwanie na utworzenie pliku...")
                time.sleep(1)
            else:
                print("Plik został utworzony!")
                break

            # TODO pomimo, że plik jest wdg aplikacji został utowrzony, to nie widać to w strukturze projektu
            #  oraz nie istnieje w nie key location przez co poniższe przekierowanie zwraca KeyError: 'Paris'
        return redirect(url_for("display_forecast.display_forecast"))

    return render_template("app.html")


@display_forecast_blueprint.route("/display_forecast")
def display_forecast():
    json_file = weather_forecast.display_weather_forecast(location, date_time)
    formatted_json = json.dumps(json_file, indent=4)
    return render_template(
        "display_forecast.html", location=location, json_data=formatted_json
    )


# if __name__ == "__main__":
#     # Dane do konfiguracji
#     FILE_NAME = "weather_data.json"
#     API_URL = "https://api.weatherapi.com/v1/current.json"
#     API_KEY = "b99a17a73c824419988144105240204"
#     LOCATION = "London"
#     date_time = "2020-01-21 10:00"
#
#     # Inicjalizacja obiektu prognozy pogody
#     weather_forecast = WeatherForecast(FILE_NAME, API_URL, API_KEY)
#
#     # Pobranie prognozy pogody lub odzyskanie danych z pliku
#     weather_forecast.fetch_weather_forecast(LOCATION, date_time)
#
#     # Wyświetlenie prognozy pogody
#     weather_forecast.display_weather_forecast(LOCATION, date_time)
