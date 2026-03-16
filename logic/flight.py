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
    airline = details.get('airline') or {}
    airline = airline.get('name', 'Unknown airline')

    aircraft = details.get('aircraft') or {}
    aircraft = aircraft.get('model') or {}
    aircraft = aircraft.get('text', flight.aircraft_code)

    airport = details.get('airport') or {}

    origin = airport.get('origin') or {}
    origin_position = origin.get('position') or {}
    origin_region = origin_position.get('region') or {}
    origin_city = origin_region.get('city', flight.origin_airport_iata)
    origin_airport = origin.get('name', origin_city)

    destination = airport.get('destination') or {}
    destination_position = destination.get('position') or {}
    destination_region = destination_position.get('region') or {}
    destination_city = destination_region.get('city', flight.destination_airport_iata)
    destination_airport = destination.get('name', destination_city)
    
    return {
        'callsign': flight.callsign,
        'number': flight.number,
        'airline': airline,
        'aircraft': aircraft,
        'origin': origin_city,
        'origin_airport': origin_airport,
        'destination': destination_city,
        'destination_airport': destination_airport,
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