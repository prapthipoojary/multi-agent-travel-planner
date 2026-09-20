def budget_agent(budget, transport_cost, hotel_cost, activity_cost, food_cost):

    total_cost = (
        transport_cost
        + hotel_cost
        + activity_cost
        + food_cost
    )

    remaining_budget = budget - total_cost

    return {
        "agent": "Budget Agent",
        "total_cost": total_cost,
        "remaining_budget": remaining_budget
    }