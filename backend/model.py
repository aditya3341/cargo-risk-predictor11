import random
from math import radians, sin, cos, sqrt, atan2

ports = {
    "Mumbai": (19.0760,72.8777),
    "Chennai": (13.0827,80.2707),
    "Kolkata": (22.5726,88.3639),
    "Singapore": (1.3521,103.8198),
    "Shanghai": (31.2304,121.4737),
    "Dubai": (25.2048,55.2708),
    "Hamburg": (53.5511,9.9937),
    "Rotterdam": (51.9244,4.4777),
    "Antwerp": (51.2194,4.4025),
    "Los Angeles": (34.0522,-118.2437),
    "New York": (40.7128,-74.0060),
    "Seattle": (47.6062,-122.3321),
    "Houston": (29.7604,-95.3698),
    "London": (51.5072,-0.1276),
    "Barcelona": (41.3851,2.1734),
    "Santos": (-23.9608,-46.3336),
    "Sydney": (-33.8688,151.2093),
    "Cape Town": (-33.9249,18.4241),
    "Durban": (-29.8587,31.0218)
}

def calculate_distance(port1, port2):

    lat1, lon1 = ports[port1]
    lat2, lon2 = ports[port2]

    R = 6371

    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)

    a = sin(dlat/2)**2 + cos(radians(lat1))*cos(radians(lat2))*sin(dlon/2)**2
    c = 2 * atan2(sqrt(a), sqrt(1-a))

    return R * c


def predict_risk(source, destination, cargo="normal", weather=None, congestion=None):

    distance = calculate_distance(source, destination)

    # Convert optional inputs
    if weather is None or weather == "":
        weather = random.randint(1,5)
    else:
        weather = int(weather)

    if congestion is None or congestion == "":
        congestion = random.randint(1,5)
    else:
        congestion = int(congestion)

    cargo_val = 1 if cargo == "fragile" else 0

    risk = weather*10 + congestion*8 + cargo_val*12 + distance*0.002

    if risk < 40:
        level = "Low Risk"
    elif risk < 70:
        level = "Medium Risk"
    else:
        level = "High Risk"

    return round(risk,2), level, distance, weather, congestion