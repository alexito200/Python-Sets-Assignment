# Task 1: Flight Route Comparison


def airline_routes():
    our_routes = {"LAX", "JFK", "CDG", "DXB"}
    competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

    common_destinations = our_routes.intersection(competitor_routes)
    
    unique_destinations = our_routes.difference(competitor_routes)
    
    unshared_destinations = our_routes.symmetric_difference(competitor_routes)

    print("Common destinations:", common_destinations)
    print("Unique destinations to our airline:", unique_destinations)
    print("Unshared destinations:", unshared_destinations)

airline_routes()
