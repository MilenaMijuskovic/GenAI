import googlemaps

def get_closest_shelters(lat, lng, radius=5000, shelters=10):
    gmaps = googlemaps.Client(key='AIzaSyDOasWCFyUrISMIqyy8w5jpPNgyUhk3yvM')

    # Search for nearby shelters
    places_result = gmaps.places_nearby(
        location=(lat, lng),
        radius=radius,
        keyword="emergency shelter"
    )

    shelters = places_result.get("results", [])[:shelters]
    return [
        {
            "name": shelter["name"],
            "address": shelter.get("vicinity", "N/A"),
            "location": shelter["geometry"]["location"]
        }
        for shelter in shelters
    ]
    

if __name__ == "__main__":
    # setup

    current_lat = 40.7128  # Example latitude (New York City)
    current_long = -74.0060  # Example longitude (New York City)

    closest_shelters = get_closest_shelters(current_lat, current_long)

    for shelter in closest_shelters:
        print(shelter["name"])
        print(shelter["address"])
        print(shelter["location"])
        print()

