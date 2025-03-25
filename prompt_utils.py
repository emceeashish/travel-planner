def get_user_prompts(destination, travel_dates, budget, preferences, bonus_details=""):
    # Create the base prompt with user inputs
    prompt = (
        f"You are a travel planning assistant. A user wants to visit {destination} from {travel_dates} "
        f"with a {budget} budget. They are interested in: {preferences}. "
    )
    # Append bonus details if available
    if bonus_details:
        prompt += bonus_details + " "
    prompt += (
        "Please generate a detailed, day-by-day travel itinerary that includes recommended activities, dining options, sightseeing, and any other relevant suggestions."
    )
    return prompt
