import streamlit as st
from prompt_utils import get_user_prompts
from itinerary_generator import generate_itinerary
from bonus_features import get_bonus_details
from dotenv import load_dotenv
import os

# Load our API key and other settings from .env
load_dotenv()

def main():
    st.title("AI-Powered Travel Planner")
    st.write("Plan your personalized travel itinerary with our AI assistant!")

    # Basic inputs from the user
    destination = st.text_input("Enter your travel destination:")
    travel_dates = st.text_input("Enter your travel dates (e.g., 2023-08-01 to 2023-08-05):")
    budget = st.text_input("Enter your budget (e.g., budget, moderate, luxury):")
    preferences = st.text_area("Enter your travel preferences (e.g., sightseeing, food, adventure):")

    # Extra optional details in an expander
    with st.expander("Bonus: Extra Preferences (Optional)"):
        dietary = st.text_input("Dietary preferences? (e.g., vegetarian, gluten-free)")
        mobility = st.text_input("Mobility concerns? (e.g., minimal walking, wheelchair accessible)")
        hotel_pref = st.text_input("Hotel preference? (e.g., budget, luxury, central)")

    if st.button("Generate Itinerary"):
        if destination and travel_dates and budget and preferences:
            st.write("Generating itinerary, please wait...")
            # Combine the bonus info (if any) into a string
            bonus_details = get_bonus_details(dietary, mobility, hotel_pref)
            # Build our full prompt from user inputs and bonus details
            prompt = get_user_prompts(destination, travel_dates, budget, preferences, bonus_details)
            # Get the itinerary from the Together.ai API
            itinerary = generate_itinerary(prompt)
            st.markdown("### Your Travel Itinerary:")
            st.write(itinerary)
        else:
            st.error("Please fill out all the required fields!")

if __name__ == "__main__":
    main()
