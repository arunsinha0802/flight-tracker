import time
from logic.flight import get_overhead_flights, get_flight_info
from logic.temperature import get_temperature
from logic.clock import get_time, get_date
from logic.audio import announce

# Track the last announced flight so we don't repeat announcements
last_announced = None

print("Flight tracker starting...")

while True:
    # Get current time and temperature
    current_time = get_time()
    current_date = get_date()
    temperature = get_temperature()

    # Check for overhead flights
    flights = get_overhead_flights()

    if flights:
        # Get details of the first flight
        info = get_flight_info(flights[0])

        # Only announce if it's a new flight
        if info['callsign'] != last_announced:
            last_announced = info['callsign']

            announcement = (
                f"{info['airline']} flight {info['number']} "
                f"from {info['origin']} to {info['destination']}, "
                f"a {info['aircraft']}, is currently overhead"
            )

            print(f"[{current_time}] FLIGHT: {announcement}")
            announce(announcement)

    else:
        last_announced = None
        print(f"[{current_time}] {current_date} | {temperature}°C | No flights overhead")

    # Wait before polling again
    time.sleep(10)