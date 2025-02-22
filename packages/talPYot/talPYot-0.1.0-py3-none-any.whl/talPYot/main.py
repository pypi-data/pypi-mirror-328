import math
import sys
import json

def DaveningAngle(coords):
	kosel = [31.7767, 35.2345]
	dLng = kosel[1] - coords[1]
	dLat = kosel[0] - coords[0]
	omg = math.atan2(dLng, dLat)
	return (math.degrees(omg))

def DrawCompass(degrees, radius=10):
    # Create the compass circle
    compass = ""
    for y in range(-radius, radius + 1):
        for x in range(-radius, radius + 1):
            distance = math.sqrt(x**2 + y**2)
            if abs(distance - radius) < 0.5:  # Approximate circle
                compass += "o"
            else:
                compass += " "
        compass += "\n"

    radians = math.radians(90 - degrees) 
    arrow_x = int(round(radius * 0.75 * math.cos(radians)))
    arrow_y = int(round(radius * 0.75 * math.sin(radians)))

    # Draw the arrow
    lines = compass.splitlines()  # Split into lines for easier manipulation
    center_y = radius
    center_x = radius

    dx = arrow_x
    dy = arrow_y
    for i in range (1, int(math.sqrt(dx**2 + dy**2)) + 1): # Arrow length
        plot_x = int(center_x + i * dx / math.sqrt(dx**2 + dy**2))
        plot_y = int(center_y - i * dy / math.sqrt(dx**2 + dy**2))
        if 0 <= plot_y < len(lines) and 0 <= plot_x < len(lines[plot_y]):
            lines[plot_y] = lines[plot_y][:plot_x] + "." + lines[plot_y][plot_x+1:]
    
    return "\n".join(lines)

if __name__ == '__main__':
    from geopy.geocoders import Nominatim
    
    geolocator = Nominatim(user_agent='myapplication')
    locationString = ""
    for i in sys.argv[1:]:
        locationString += i + " "
    location = geolocator.geocode(locationString)
    if location is None:
        results = {
            "error": "Location Not Found"
        }
        print(json.dumps(results, indent=4))
        sys.exit(1)
    else:
        lat = float(location.raw["lat"])
        lon = float(location.raw["lon"])
        degrees = DaveningAngle([lat, lon])
        results = {
            "LocationName": location.raw["display_name"],
            "DaveningAngle": degrees,
            "DirectionCompass": DrawCompass(degrees)
        }
        print(json.dumps(results, indent=4))
        print(results['DirectionCompass'])
    
