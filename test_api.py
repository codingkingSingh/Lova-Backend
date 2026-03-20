import os
import requests
from dotenv import load_dotenv

# 1. Load the secret vault (.env)
load_dotenv()
api_key = os.getenv("BESTTIME_API_KEY")

# 2. Set up the BestTime API details
url = "https://besttime.app/api/v1/forecasts"
params = {
    "api_key_private": api_key,
    "venue_name": "McDonald's",
    "venue_address": "20605 Hwy 365, North Little Rock, AR 72113" # You can change this to a real address near you later!
}

print("Dialing the BestTime API...")

# 3. Try to make the call
try:
    response = requests.post(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        print("\n🎉 SUCCESS! Here is the raw foot-traffic data:")
        print(data)
    else:
        print(f"\n⚠️ ERROR: The API returned a status code {response.status_code}")
        print("Message from server:", response.text)

except Exception as e:
    print(f"\n❌ CRITICAL ERROR: Could not connect to the internet. {e}")