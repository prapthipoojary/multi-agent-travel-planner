def hotel_agent(destination, budget):

    hotel_budget = int(budget * 0.30)

    destination_lower = destination.lower()

    hotels = {
        "goa": [
            "Baga",
            "Calangute",
            "Candolim",
            "Panaji"
        ],

        "manali": [
            "Old Manali",
            "Mall Road",
            "Manali town"
        ],

        "bangalore": [
            "MG Road",
            "Indiranagar",
            "Koramangala"
        ],

        "mysore": [
            "Near Mysore Palace",
            "VV Mohalla",
            "Hebbal"
        ],

        "mumbai": [
            "Colaba",
            "Andheri",
            "Bandra"
        ]
    }

    recommended_areas = hotels.get(
        destination_lower,
        [
            f"Central area of {destination}",
            f"Near major attractions in {destination}",
            f"Near public transport in {destination}"
        ]
    )

    return {
        "agent": "Hotel Agent",
        "destination": destination,
        "suggestion": (
            f"Look for budget-friendly accommodation in "
            f"{', '.join(recommended_areas)}."
        ),
        "recommended_areas": recommended_areas,
        "estimated_cost": hotel_budget
    }