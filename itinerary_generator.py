import requests
import streamlit as st

# Make sure our .env file is loaded here as well

def generate_itinerary(prompt):
    # Get the API key from the environment
    api_key = st.secrets["TOGETHER_API_KEY"]
    if not api_key:
        return "Error: API key not set."

    # Correct endpoint for chat-style completions
    url = "https://api.together.xyz/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    # Build the data payload using a chat message format
    data = {
        "model": "mistralai/Mixtral-8x7B-Instruct-v0.1",
        "messages": [
            {"role": "system", "content": "You are a helpful travel planning assistant."},
            {"role": "user", "content": prompt}
        ],
        "max_tokens": 800,
        "temperature": 0.7
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()  # This will throw an error for bad responses
        result = response.json()
        # Return the generated itinerary text
        return result['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"Error generating itinerary: {e}"
