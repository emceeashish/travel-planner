# AI-Powered Travel Planner

This project generates **personalized travel itineraries** using [Together.ai](https://together.ai)'s **Mixtral-8x7B-Instruct** model via API.  
The app is built with **Streamlit** and supports optional features (dietary needs, mobility concerns, and hotel preferences) for extra personalization.

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
├── .env                  # Your Together.ai API key (not committed)
├── app.py                # Streamlit app to collect inputs and display output
├── bonus_features.py     # Handles extra preferences (dietary, mobility, hotel)
├── prompt_utils.py       # Builds the prompt from user inputs
├── itinerary_generator.py# Calls the Together.ai API
├── requirements.txt      # Project dependencies
└── README.md             # This file
```

---

## Setup

1. **Clone the repository**:
```bash
git clone https://github.com/emceeashish/travel-planner.git
cd travel-planner
```

2. *(Optional)* **Create a new conda environment** or use an existing one:
```bash
conda create -n travelplanner python=3.10
conda activate travelplanner
```

3. **Install dependencies**:
```bash
pip install -r requirements.txt
```

4. **Create a `.env` file** in the project root with your Together.ai API key:
```bash
# .env
TOGETHER_API_KEY=your_api_key_here
```
Replace `your_api_key_here` with your **actual** API key.  

5. **Run the app**:
```bash
streamlit run app.py
```
Your browser should open automatically, showing the Streamlit interface.

---

## Usage

1. **Enter Basic Details**  
   - **Destination** (e.g., “Kyoto”)  
   - **Travel Dates** (e.g., “2025-04-01 to 2025-04-04”)  
   - **Budget** (e.g., “moderate”)  
   - **Preferences** (e.g., “culture, temples, food, walkable places”)

2. **(Optional) Bonus Inputs**  
   - Dietary needs (e.g., “vegetarian”)  
   - Mobility concerns (e.g., “minimal walking”)  
   - Hotel preferences (e.g., “central”)

3. **Generate Itinerary**  
   - Click “Generate Itinerary”  
   - The AI will create a **day-by-day travel plan** tailored to your inputs

---

## Example Input/Output

**Example Inputs**  
- **Destination:** Kyoto  
- **Dates:** 2025-04-01 to 2025-04-04  
- **Budget:** Moderate  
- **Preferences:** Culture, temples, food, walkable places  
- **Dietary:** Vegetarian  
- **Mobility:** Minimal walking  
- **Hotel Preference:** Central  

**Sample Itinerary (Shortened)**

```
Day 1:
- Morning: Arrive in Kyoto, check in at a central, budget-friendly hotel.
- Afternoon: Visit Kinkaku-ji (Golden Pavilion). It's accessible for minimal walking.
- Evening: Dinner at Shigetsu for vegetarian shojin-ryori temple cuisine.

Day 2:
- Morning: Explore Fushimi Inari Shrine (lower trails for mobility concerns).
- Afternoon: Philosopher's Path and Ginkaku-ji (Silver Pavilion).
- Evening: Try a gourmet vegetarian meal at Ain Soph Journey Kyoto.
...
```

---

## Bonus Features

- **Flexible Input Formats**  
  Accepts extra details like dietary, mobility, and hotel preferences for more nuanced itineraries.  
- **Enhanced Personalization**  
  Integrates bonus inputs into the prompt, refining the final travel plan to meet specific needs.

---

## Future Enhancements

- **Live Web Search**  
  Pull real-time events or attraction data.  
- **Chat Refinements**  
  Let users adjust or regenerate parts of the itinerary (e.g., “replan Day 2 with more cultural spots”).  
- **Export Options**  
  Generate PDFs or sync with user calendars for better planning.

---
