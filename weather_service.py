import requests
from config import API_KEY, BASE_URL


def get_location_key(city_name):
    url = f"{BASE_URL}/locations/v1/cities/search"
    params = {"apikey": API_KEY, "q": city_name}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        if data:
            return data[0]["Key"]
    return None


def get_weather_forecast(location_key):
    url = f"{BASE_URL}/forecasts/v1/daily/1day/{location_key}"
    params = {"apikey": API_KEY, "metric": True}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    return None
