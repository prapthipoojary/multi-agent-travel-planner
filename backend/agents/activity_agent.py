def activity_agent(destination, budget):

    activity_budget = int(budget * 0.20)

    destination_lower = destination.lower()

    activities = {
        "goa": [
            "Visit Baga Beach",
            "Explore Fort Aguada",
            "Visit Basilica of Bom Jesus",
            "Explore Panjim",
            "Enjoy a sunset at a popular beach"
        ],

        "manali": [
            "Visit Solang Valley",
            "Explore Mall Road",
            "Visit Hadimba Temple",
            "Enjoy mountain views",
            "Explore Old Manali"
        ],

        "bangalore": [
            "Visit Lalbagh Botanical Garden",
            "Explore Cubbon Park",
            "Visit Bangalore Palace",
            "Explore Vidhana Soudha",
            "Enjoy local food"
        ],

        "mysore": [
            "Visit Mysore Palace",
            "Explore Brindavan Gardens",
            "Visit Chamundi Hill",
            "Explore Devaraja Market",
            "Try Mysore's local food"
        ],

        "mumbai": [
            "Visit Gateway of India",
            "Explore Marine Drive",
            "Visit Chhatrapati Shivaji Maharaj Terminus",
            "Explore Colaba",
            "Try local street food"
        ]
    }

    selected_activities = activities.get(
        destination_lower,
        [
            f"Explore popular attractions in {destination}",
            f"Visit famous landmarks in {destination}",
            f"Explore local markets in {destination}",
            "Try popular local food",
            "Enjoy local sightseeing"
        ]
    )

    return {
        "agent": "Activity Agent",
        "destination": destination,
        "suggestion": f"Recommended activities in {destination}.",
        "activities": selected_activities,
        "estimated_cost": activity_budget
    }