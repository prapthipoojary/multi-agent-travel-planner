def food_agent(destination, budget):

    food_budget = int(budget * 0.15)

    destination_lower = destination.lower()

    foods = {
        "goa": [
            "Goan fish curry and rice",
            "Prawn curry",
            "Chicken xacuti",
            "Bebinca",
            "Local seafood"
        ],

        "manali": [
            "Siddu",
            "Thukpa",
            "Momos",
            "Tibetan noodles",
            "Local Himachali dishes"
        ],

        "bangalore": [
            "Masala dosa",
            "Idli and vada",
            "Bisi bele bath",
            "Ragi mudde",
            "South Indian meals"
        ],

        "mysore": [
            "Mysore masala dosa",
            "Mysore pak",
            "Idli and vada",
            "South Indian meals",
            "Local snacks"
        ],

        "mumbai": [
            "Vada pav",
            "Pav bhaji",
            "Misal pav",
            "Bombay sandwich",
            "Local street food"
        ]
    }

    recommended_foods = foods.get(
        destination_lower,
        [
            f"Try popular local food in {destination}",
            "Explore local restaurants",
            "Try traditional dishes",
            "Visit popular food markets"
        ]
    )

    return {
        "agent": "Food Agent",
        "destination": destination,
        "suggestion": (
            f"Recommended food experiences in {destination}."
        ),
        "recommended_foods": recommended_foods,
        "estimated_cost": food_budget
    }