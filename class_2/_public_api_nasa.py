# 📘 Call a public REST API and extract structured data (JSON to DataFrame)

import requests
import pandas as pd

# NASA asteroid data API
url = "https://api.nasa.gov/neo/rest/v1/neo/browse"
params = {
    "api_key": "DEMO_KEY"  # Use your own key if rate-limited
}

response = requests.get(url, params=params)
data = response.json()

# Convert nested JSON to DataFrame
neos = data['near_earth_objects']
df = pd.json_normalize(neos)

# Preview
df[['id', 'name', 'absolute_magnitude_h', 'is_potentially_hazardous_asteroid']].head()

# === 🏠 HOMEWORK ===
# 1. Try other APIs (e.g., https://api.publicapis.org/entries).
# 2. Use `.shape` and `.describe()` to explore numeric fields.
# 3. Save results to CSV using df.to_csv("output.csv").
