\# 🌍 Multi-Agent Travel Planner



An AI-powered travel planning web application that creates personalized trip plans based on the user's destination, budget, and travel dates.



\## ✨ Features



\- 🚌 Transport recommendations

\- 🏨 Hotel/accommodation recommendations

\- 🏖️ Activity recommendations

\- 🍴 Food recommendations

\- 💰 Budget calculation

\- 🛡️ Emergency/contingency budget

\- 🗓️ Date-based itinerary generation

\- 🤖 Multi-agent architecture

\- 🌐 Web-based user interface



\## 🏗️ Project Architecture



The application uses multiple specialized agents:



```text

User

&#x20; ↓

Frontend

&#x20; ↓

FastAPI Backend

&#x20; ↓

┌───────────────────────┐

│    Travel Agents      │

├───────────────────────┤

│ Transport Agent       │

│ Hotel Agent           │

│ Activity Agent        │

│ Food Agent            │

│ Budget Agent          │

│ Contingency Agent     │

│ Final Planner Agent   │

└───────────────────────┘

&#x20; ↓

Personalized Travel Plan

