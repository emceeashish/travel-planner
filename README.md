# AI-Powered Travel Planner

This project generates **personalized travel itineraries** using [Together.ai](https://together.ai)'s **Mixtral-8x7B-Instruct** model via an API. The application is built with **Streamlit** and includes optional features for dietary requirements, mobility concerns, and hotel preferences, allowing for more personalized itineraries.

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

```
ai_travel_planner/
├── .env                  # Contains the Together.ai API key (not committed)
├── app.py                # Main Streamlit app for input collection and output display
├── bonus_features.py     # Processes extra preferences (dietary, mobility, hotel)
├── prompt_utils.py       # Builds the prompt from user inputs
├── itinerary_generator.py# Calls the Together.ai API to generate itineraries
├── requirements.txt      # Lists required Python packages
└── README.md             # This file
```

---

## Setup

1. **Repository Cloning**  
   ```bash
   git clone https://github.com/emceeashish/travel-planner.git
   cd travel-planner
   ```

2. **(Optional) Conda Environment**  
   ```bash
   conda create -n travelplanner python=3.10
   conda activate travelplanner
   ```
   *(A preferred Python environment may be used if conda is not desired.)*

3. **Install Dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Configuration**  
   Create a `.env` file at the project root to store the Together.ai API key:
   ```bash
   # .env
   TOGETHER_API_KEY=EXAMPLE_KEY
   ```
   > The `TOGETHER_API_KEY` variable is used for authenticating requests to the Together.ai API.  
   > This key should remain private and not be committed to any public repository.

5. **Run the App**  
   ```bash
   streamlit run app.py
   ```
   A browser window should open automatically, showing the Streamlit interface.

---

## Usage

1. **Basic Details**  
   - Destination (e.g., “Kyoto”)  
   - Travel Dates (e.g., “2025-04-01 to 2025-04-04”)  
   - Budget (e.g., “moderate”)  
   - Preferences (e.g., “culture, temples, food, walkable places”)

2. **(Optional) Bonus Inputs**  
   - Dietary requirements (e.g., “vegetarian”)  
   - Mobility concerns (e.g., “minimal walking”)  
   - Hotel preferences (e.g., “central”)

3. **Generate the Itinerary**  
   - Click **Generate Itinerary**  
   - A **day-by-day travel plan** will be generated based on the inputs

---

## Example Input/Output

**Example Inputs**  
- Destination: Kyoto  
- Dates: 2025-04-01 to 2025-04-04  
- Budget: Moderate  
- Preferences: Culture, temples, food, walkable places  
- Dietary: Vegetarian  
- Mobility: Minimal walking  
- Hotel Preference: Central  

**Sample Output (Shortened)**

```
Day 1:
- Morning: Arrive in Kyoto, check into a centrally located hotel.
- Afternoon: Visit Kinkaku-ji (Golden Pavilion), accessible for minimal walking.
- Evening: Try vegetarian temple cuisine at Shigetsu.

Day 2:
- Morning: Explore Fushimi Inari Shrine (lower trails for mobility considerations).
- Afternoon: Stroll along the Philosopher's Path and stop by Ginkaku-ji (Silver Pavilion).
- Evening: Enjoy a vegetarian meal at Ain Soph Journey Kyoto.
...
```

---

## Bonus Features

- **Flexible Input Formats**  
  Includes additional details such as dietary restrictions, mobility needs, and hotel preferences to refine the itinerary.
- **Enhanced Personalization**  
  Integrates bonus inputs into the final output, ensuring closer alignment with user requirements.

---

## Future Enhancements

- **Live Web Search**  
  Potential integration for real-time data on events or nearby activities.
- **Chat Refinements**  
  Option to adjust or regenerate specific parts of the itinerary (e.g., “add more cultural spots on Day 2”).
- **Export Options**  
  Provide PDF generation or calendar syncing for streamlined travel planning.

---
