def contingency_agent(budget):

    contingency_budget = int(budget * 0.10)

    return {
        "agent": "Contingency Agent",
        "suggestion": "Keep this amount reserved for unexpected travel expenses.",
        "estimated_cost": contingency_budget
    }