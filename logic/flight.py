from FlightRadar24 import FlightRadar24API
from config import LOCATION_LAT, LOCATION_LON, SEARCH_RADIUS_KM

# Initialise the FlightRadar24 API
fr = FlightRadar24API()

def get_overhead_flights():
    # Convert radius from km to metres for the API
    radius_m = SEARCH_RADIUS_KM * 1000

    # Get the bounding box around our location
    bounds = fr.get_bounds_by_point(LOCATION_LAT, LOCATION_LON, radius_m)

    # Fetch all flights within the bounding box
    flights = fr.get_flights(bounds=bounds)

    # Filter to only airborne flights
    airborne = [f for f in flights if f.on_ground == 0 and f.altitude > 0]

    return airborne

def get_flight_info(flight):
    # Fetch detailed information for a specific flight
    details = fr.get_flight_details(flight)

    # Extract the fields we need with safe fallbacks
    airline = details.get('airline', {}).get('name', 'Unknown airline')
    aircraft = details.get('aircraft', {}).get('model', {}).get('text', flight.aircraft_code)

    origin_city = (details.get('airport', {})
                   .get('origin', {})
                   .get('position', {})
                   .get('region', {})
                   .get('city', flight.origin_airport_iata))

    destination_city = (details.get('airport', {})
                        .get('destination', {})
                        .get('position', {})
                        .get('region', {})
                        .get('city', flight.destination_airport_iata))

    return {
        'callsign': flight.callsign,
        'number': flight.number,
        'airline': airline,
        'aircraft': aircraft,
        'origin': origin_city,
        'destination': destination_city,
        'altitude': flight.altitude,
    }


# Only runs when executing this file directly
if __name__ == "__main__":
    print("Searching for overhead flights...")
    flights = get_overhead_flights()

    if flights:
        print(f"Found {len(flights)} airborne flight(s)")
        info = get_flight_info(flights[0])
        print(info)
    else:
        print("No airborne flights found in range")