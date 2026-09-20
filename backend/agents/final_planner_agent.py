from datetime import datetime


def final_planner_agent(
    destination,
    start_date,
    end_date,
    transport,
    hotel,
    activity,
    food,
    budget_summary,
    contingency
):

    # Calculate number of travel days
    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")

    number_of_days = (end - start).days + 1

    if number_of_days < 1:
        number_of_days = 1

    # Get destination-specific activities
    activities_list = activity.get("activities", [])

    itinerary = []

    for day_number in range(1, number_of_days + 1):

        if day_number == 1:

            title = "Arrival and Local Exploration"

            day_activities = [
                f"Travel to {destination}",
                "Check in to the hotel"
            ]

            if activities_list:
                day_activities.append(activities_list[0])

            day_activities.append(
                "Enjoy local food for dinner"
            )

        elif day_number == number_of_days:

            title = "Relaxation and Return"

            day_activities = []

            if len(activities_list) > 1:
                day_activities.append(
                    activities_list[-1]
                )

            day_activities.extend([
                "Enjoy a relaxed morning",
                "Check out from the hotel",
                f"Return from {destination}"
            ])

        else:

            title = "Sightseeing and Activities"

            # Select activities for this day
            if activities_list:

                index = day_number - 1

                selected = activities_list[
                    index % len(activities_list)
                ]

                day_activities = [
                    selected,
                    "Explore nearby places",
                    "Enjoy local food"
                ]

            else:

                day_activities = [
                    f"Explore popular attractions in {destination}",
                    "Explore local places",
                    "Enjoy local food"
                ]

        itinerary.append({
            "day": f"Day {day_number}",
            "title": title,
            "activities": day_activities
        })

    return {

        "agent": "Final Planner Agent",

        "destination": destination,

        "travel_dates": f"{start_date} to {end_date}",

        "number_of_days": number_of_days,

        "transport": transport["suggestion"],

        "hotel": hotel["suggestion"],

        "activities": activity["suggestion"],

        "food": food["suggestion"],

        "total_cost": budget_summary["total_cost"],

        "remaining_budget": budget_summary["remaining_budget"],

        "contingency": contingency["estimated_cost"],

        "itinerary": itinerary,

        "message": (
            f"Your {number_of_days}-day trip to "
            f"{destination} has been planned successfully!"
        )
    }