import requests
import time
from logic.clock import get_time_of_day

SONOS_URL = "http://localhost:5005"
ROOM_NAME = "Kitchen"

def _say(text):
    encoded = requests.utils.quote(text)
    requests.get(f"{SONOS_URL}/{ROOM_NAME}/say/{encoded}")

def announce(text):
    _say(text)

def greeting():
    text = f"Good {get_time_of_day()} Mr. Ellis. Your flight tracker is online."
    _say(text)