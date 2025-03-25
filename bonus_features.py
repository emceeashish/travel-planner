def get_bonus_details(dietary, mobility, hotel_pref):
    # Start with an empty string for extra details
    details = ""
    if dietary:
        details += f"Dietary preferences: {dietary}. "
    if mobility:
        details += f"Mobility concerns: {mobility}. "
    if hotel_pref:
        details += f"Hotel preference: {hotel_pref}. "
    return details
