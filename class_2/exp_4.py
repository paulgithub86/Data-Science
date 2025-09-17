# 📘 Access OpenWeatherMap API (demo) and parse semi-structured JSON

import requests
import pandas as pd

url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": 25.03,  # Taipei
    "longitude": 121.56,
    "hourly": "temperature_2m",
    "forecast_days": 1,
    "timezone": "Asia/Taipei"
}

response = requests.get(url, params=params)
data = response.json()

# Convert hourly temperature to DataFrame
df = pd.DataFrame({
    "time": data["hourly"]["time"],
    "temp": data["hourly"]["temperature_2m"]
})

df.head()

# === 🏠 HOMEWORK ===
# 1. Plot temperature vs. time using matplotlib.
# 2. Change location to your hometown (adjust lat/lon).
