import requests
from config import LOCATION_LAT, LOCATION_LON

def get_temperature():
    # Build the API URL using coordinates from config
    # We only request temperature_2m — no unnecessary data
    url = (
        f"https://api.open-meteo.com/v1/forecast"
        f"?latitude={LOCATION_LAT}"
        f"&longitude={LOCATION_LON}"
        f"&current=temperature_2m"
    )
    
    # Make the HTTP GET request to Open-Meteo
    response = requests.get(url)
    
    # Convert the JSON response into a Python dictionary
    data = response.json()
    
    # Navigate into the dictionary to extract just the temperature value
    temperature = data["current"]["temperature_2m"]
    
    return temperature


# Only runs when executing this file directly, not when imported
if __name__ == "__main__":
    print(get_temperature())