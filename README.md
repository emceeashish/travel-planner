# AI-Powered Travel Planner

This project generates **personalized travel itineraries** using [Together.ai](https://together.ai)'s **Mixtral-8x7B-Instruct** model via API.  
The app is built with **Streamlit** and includes extra features (e.g., dietary needs, mobility concerns, hotel preferences) for even more personalization.

---

## Table of Contents

1. [Project Structure](#project-structure)  
2. [Setup](#setup)  
3. [Usage](#usage)  
4. [Example Input/Output](#example-inputoutput)  
5. [Bonus Features](#bonus-features)  
6. [Future Enhancements](#future-enhancements)

---

## Project Structure

ai_travel_planner/ ├── .env # Your Together.ai API key (not committed) ├── app.py # Streamlit app to collect inputs and display output ├── bonus_features.py # Handles extra preferences (dietary, mobility, hotel) ├── prompt_utils.py # Builds the prompt from user inputs ├── itinerary_generator.py# Calls the Together.ai API ├── requirements.txt # Project dependencies └── README.md # This file

yaml
Copy
Edit

---

## Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/emceeashish/travel-planner.git
   cd travel-planner
(Optional) Create a new conda environment or use an existing one:

bash
Copy
Edit
conda create -n travelplanner python=3.10
conda activate travelplanner
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Create a .env file in the project root with your Together.ai API key:

bash
Copy
Edit
# .env
TOGETHER_API_KEY=your_api_key_here
Replace your_api_key_here with your actual API key.
Never commit this key to any public repo.

Run the Streamlit app:

bash
Copy
Edit
streamlit run app.py
This will open the app in your default web browser.

Usage
Enter Basic Details

Destination (e.g., Kyoto)

Travel Dates (e.g., 2025-04-01 to 2025-04-04)

Budget (e.g., moderate)

Preferences (e.g., culture, temples, food, walkable places)

(Optional) Bonus Inputs

Dietary needs (e.g., vegetarian)

Mobility concerns (e.g., minimal walking)

Hotel preferences (e.g., central)

Generate Itinerary

Click "Generate Itinerary"

Wait for the AI to create a day-by-day travel plan tailored to your inputs

Example Input/Output
Example Inputs

Destination: Kyoto

Dates: 2025-04-01 to 2025-04-04

Budget: Moderate

Preferences: Culture, temples, food, walkable places

Dietary: Vegetarian

Mobility: Minimal walking

Hotel Preference: Central

Sample Itinerary (Shortened)

yaml
Copy
Edit
Day 1:
- Morning: Arrive in Kyoto, check in at a central, budget-friendly hotel.
- Afternoon: Visit Kinkaku-ji (Golden Pavilion). It's accessible for minimal walking.
- Evening: Dinner at Shigetsu for vegetarian shojin-ryori temple cuisine.

Day 2:
- Morning: Explore Fushimi Inari Shrine (enjoy lower shrine areas if mobility is limited).
- Afternoon: Philosopher's Path (flat, paved) and Ginkaku-ji (Silver Pavilion).
- Evening: Try a gourmet vegetarian meal at Ain Soph Journey Kyoto.
...
Bonus Features
Flexible Input Formats: Accepts extra details (dietary, mobility, hotel preference) for more nuanced itineraries.

Enhanced Personalization: The prompt includes bonus details, refining the final travel plan.

Future Enhancements
Live Web Search: Fetch real-time attraction data or events.

Chat Refinements: Let users say “Regenerate Day 2” or “Add more cultural spots” for iterative planning.

Export Options: Generate PDFs or sync with a calendar for easy scheduling.
