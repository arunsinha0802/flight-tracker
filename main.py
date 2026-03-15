import time
from logic.flight import get_overhead_flights, get_flight_info
from logic.temperature import get_temperature
from logic.clock import get_time, get_date
from logic.audio import announce

# Track announced flights with timestamps
# Format: { callsign: timestamp_when_announced }
announced_flights = {}

# How long before we allow re-announcing the same flight (30 minutes)
REANNOUNCE_AFTER_SECONDS = 1800

print("Flight tracker starting...")

while True:
    current_time = get_time()
    current_date = get_date()
    temperature = get_temperature()
    temp_display = f"{temperature}°C" if temperature is not None else "N/A"

    flights = get_overhead_flights()

    if flights:
        info = get_flight_info(flights[0])
        callsign = info['callsign']
        now = time.time()

        # Check if we've announced this flight recently
        last_time = announced_flights.get(callsign, 0)
        time_since = now - last_time

        if time_since > REANNOUNCE_AFTER_SECONDS:
            announced_flights[callsign] = now

            announcement = (
                f"{info['airline']} flight {info['number']} "
                f"from {info['origin']} to {info['destination']}, "
                f"a {info['aircraft']}"
            )

            print(f"[{current_time}] FLIGHT: {announcement}")
            announce(announcement)
        else:
            print(f"[{current_time}] {callsign} still overhead — already announced")

    else:
        print(f"[{current_time}] {current_date} | {temp_display} | No flights overhead")

    time.sleep(10)