import csv
import googlemaps

def get_closest_shelters(lat, lng, radius=50000, max_shelters=25):
    gmaps = googlemaps.Client(key='AIzaSyDOasWCFyUrISMIqyy8w5jpPNgyUhk3yvM')

    # Search for nearby shelters
    places_result = gmaps.places_nearby(
        location=(lat, lng),
        radius=radius,
        keyword="emergency shelter"
    )

    shelters = places_result.get("results", [])
    return [
        {
            "name": shelter["name"],
            "address": shelter.get("vicinity", "N/A"),
            "location": shelter["geometry"]["location"]
        }
        for shelter in shelters
    ]
    
def save_shelters_to_csv(shelters, filename="shelters.csv"):
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "address", "location"])
        writer.writeheader()
        writer.writerows(shelters)

if __name__ == "__main__":
    current_lat = 40.7128  # Example latitude (New York City)
    current_long = -74.0060  # Example longitude (New York City)

    closest_shelters = get_closest_shelters(current_lat, current_long)

    save_shelters_to_csv(closest_shelters)

