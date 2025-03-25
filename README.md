# AI-Powered Travel Planner

This project generates personalized travel itineraries using [Together.ai](https://together.ai)'s **Mixtral-8x7B-Instruct** model via API. The app is built with **Streamlit** and includes bonus features for extra personalization.

## Project Structure

ai_travel_planner/ ├── .env # Contains your Together.ai API key. ├── app.py # Main Streamlit app to collect user input and display the itinerary. ├── bonus_features.py # Processes optional extra input like dietary needs, mobility concerns, and hotel preferences. ├── prompt_utils.py # Builds a detailed prompt from user inputs. ├── itinerary_generator.py # Calls the Together.ai API to generate the itinerary. ├── requirements.txt # Lists required packages.

bash
Copy

## Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/emceeashish/travel-planner.git
   cd travel-planner
(Optional) Create a new conda environment or use your existing one:

bash
Copy
conda create -n travelplanner python=3.10
conda activate travelplanner
Install dependencies:

bash
Copy
pip install -r requirements.txt
Create a .env file in the project root with your Together.ai API key:

env
Copy
TOGETHER_API_KEY=your_api_key_here
Replace your_api_key_here with your actual API key. (Do not share this key publicly.)

Run the app:

bash
Copy
streamlit run app.py
Usage
Enter your travel details:
Fill in your destination, travel dates, budget, and travel preferences.

Bonus Features (Optional):
Provide extra details like dietary preferences, mobility concerns, and hotel preferences for an even more refined itinerary.

Generate Itinerary:
Click the "Generate Itinerary" button to receive a detailed, day-by-day travel itinerary tailored to your inputs.

Example
Sample Inputs:

Destination: Kyoto

Travel Dates: 2025-04-01 to 2025-04-04

Budget: Moderate

Preferences: Culture, temples, food, walkable places

Bonus (Optional):

Dietary: Vegetarian

Mobility: Minimal walking

Hotel Preference: Central

The AI will produce a personalized itinerary that covers each day of your trip, suggesting activities, dining options, and sightseeing spots that match your criteria.

Bonus Features
Flexible Input Formats: Accepts extra details like dietary restrictions, mobility needs, and hotel preferences.

Enhanced Personalization: Integrates bonus inputs into the itinerary prompt for a more tailored travel plan.

Future Enhancements
Integrate web search for live attraction data.

Enable chat-based interactions for itinerary refinement.

Export itineraries to PDF or calendar applications.
