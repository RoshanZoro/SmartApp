import openmeteo_requests

import pandas as pd
import requests_cache
from retry_requests import retry
from datetime import datetime, UTC

# Setup the Open-Meteo API client with cache and retry on error
cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
openmeteo = openmeteo_requests.Client(session = retry_session)

url = "https://api.open-meteo.com/v1/forecast"
params = {
	"latitude": 52.0908,
	"longitude": 5.1222,
	"hourly": ["temperature_2m", "relative_humidity_2m", "wind_speed_10m", "precipitation_probability", "precipitation", "cloud_cover"],
	"current": "temperature_2m",
	"timezone": "Europe/Berlin",
	"forecast_days": 1,
	"forecast_hours": 1,
}
responses = openmeteo.weather_api(url, params=params)
response = responses[0]
current = response.Current()
current_temperature_2m = current.Variables(0).Value()
hourly = response.Hourly()
hourly_temperature_2m = hourly.Variables(0).ValuesAsNumpy()
hourly_relative_humidity_2m = hourly.Variables(1).ValuesAsNumpy()
hourly_wind_speed_10m = hourly.Variables(2).ValuesAsNumpy()
hourly_precipitation_probability = hourly.Variables(3).ValuesAsNumpy()
hourly_precipitation = hourly.Variables(4).ValuesAsNumpy()
hourly_cloud_cover = hourly.Variables(5).ValuesAsNumpy()

hourly_data = {"date": pd.date_range(
	start = pd.to_datetime(hourly.Time(), unit = "s", utc = True),
	end = pd.to_datetime(hourly.TimeEnd(), unit = "s", utc = True),
	freq = pd.Timedelta(seconds = hourly.Interval()),
	inclusive = "left"
)}

unixTime = current.Time()
temp = int(current_temperature_2m)
utc_time = datetime.fromtimestamp(unixTime, UTC)
timeFormat = utc_time.strftime("%Y-%m-%d %H:%M:%S %Z")
regen = int(hourly_precipitation)
print("UTC:", timeFormat)
print("Het is momenteel", round(temp) , " graden")
print("Er is momenteel" , regen, "% kans op regen")
