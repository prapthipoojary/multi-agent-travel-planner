def transport_agent(destination, budget):

    transport_budget = int(budget * 0.25)

    destination_lower = destination.lower()

    transport_options = {
        "goa": [
            "Flight to Goa International Airport",
            "Train to Madgaon or Vasco da Gama",
            "Bus from nearby cities",
            "Local taxi or rental scooter"
        ],

        "manali": [
            "Flight to Chandigarh followed by road travel",
            "Volvo bus to Manali",
            "Train to Chandigarh followed by bus",
            "Local taxi for sightseeing"
        ],

        "bangalore": [
            "Flight to Kempegowda International Airport",
            "Train to Bengaluru",
            "Bus from nearby cities",
            "Metro and local cab services"
        ],

        "mysore": [
            "Train to Mysuru",
            "Bus from Bengaluru",
            "Private cab",
            "Local auto or taxi"
        ],

        "mumbai": [
            "Flight to Mumbai",
            "Train to Mumbai",
            "Bus from nearby cities",
            "Local train, metro or taxi"
        ]
    }

    recommended_transport = transport_options.get(
        destination_lower,
        [
            f"Flight or train to {destination}",
            f"Bus services to {destination}",
            "Local taxi or public transport"
        ]
    )

    return {
        "agent": "Transport Agent",
        "destination": destination,
        "suggestion": (
            f"Recommended transportation options for {destination}."
        ),
        "transport_options": recommended_transport,
        "estimated_cost": transport_budget
    }