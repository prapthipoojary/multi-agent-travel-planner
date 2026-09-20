from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from backend.agents.transport_agent import transport_agent
from backend.agents.hotel_agent import hotel_agent
from backend.agents.activity_agent import activity_agent
from backend.agents.food_agent import food_agent
from backend.agents.budget_agent import budget_agent
from backend.agents.final_planner_agent import final_planner_agent
from backend.agents.contingency_agent import contingency_agent

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TripRequest(BaseModel):
    destination: str
    budget: int
    start_date: str
    end_date: str


@app.get("/")
def home():
    return {
        "message": "Multi-Agent Travel Planner is working!"
    }


@app.post("/plan-trip")
def plan_trip(trip: TripRequest):

    transport = transport_agent(
        trip.destination,
        trip.budget
    )

    hotel = hotel_agent(
        trip.destination,
        trip.budget
    )
    activity = activity_agent(
    trip.destination,
    trip.budget
    )

    food = food_agent(
    trip.destination,
    trip.budget
    )

    budget_result = budget_agent(
    trip.budget,
    transport["estimated_cost"],
    hotel["estimated_cost"],
    activity["estimated_cost"],
    food["estimated_cost"]
    )

    contingency = contingency_agent(
    trip.budget
    )

    final_plan = final_planner_agent(
    trip.destination,
    trip.start_date,
    trip.end_date,
    transport,
    hotel,
    activity,
    food,
    budget_result,
    contingency
    )


    return {
        "destination": trip.destination,
        "budget": trip.budget,
        "start_date": trip.start_date,
        "end_date": trip.end_date,
        "transport": transport,
        "hotel": hotel,
        "activity": activity,
        "food": food,
        "budget_summary": budget_result,
        "contingency": contingency,
        "final_plan": final_plan
    }