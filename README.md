# AI-Powered Travel Planner

This project generates personalized travel itineraries using Together.ai's Mixtral-8x7B-Instruct model via API. The app is built with Streamlit and includes bonus features for extra personalization.

## Project Structure

- **.env**: Contains your Together.ai API key.
- **app.py**: Main Streamlit app to collect user input and display the itinerary.
- **bonus_features.py**: Processes optional extra input like dietary needs and hotel preferences.
- **prompt_utils.py**: Builds a detailed prompt from user inputs.
- **itinerary_generator.py**: Calls the Together.ai API to generate the itinerary.
- **requirements.txt**: Lists required packages.

## Setup

1. Clone the repository.
2. (Optional) Create a new conda environment or use your existing one.
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
