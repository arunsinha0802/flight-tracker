import requests
from config import LOCATION_LAT, LOCATION_LON

def get_temperature():
    # Build the API URL using coordinates from config
    url = (
        f"https://api.open-meteo.com/v1/forecast"
        f"?latitude={LOCATION_LAT}"
        f"&longitude={LOCATION_LON}"
        f"&current=temperature_2m"
    )

    try:
        # Make the HTTP GET request to Open-Meteo
        response = requests.get(url, timeout=5)

        # Convert the JSON response into a Python dictionary
        data = response.json()

        # Navigate into the dictionary to extract just the temperature value
        return data["current"]["temperature_2m"]

    except Exception:
        # If anything goes wrong return None silently
        return None


if __name__ == "__main__":
    print(get_temperature())