import google.generativeai as palm
import os
from dotenv import load_dotenv

# Load the environment variables
load_dotenv()
palm_api_key = os.environ.get("PALM_API_KEY")


# Create a config.
palm.configure(api_key=palm_api_key)
model = palm.GenerativeModel(model_name="gemini-1.5-flash-8b-exp-0924")
# print(list(palm.list_models()))


# Generate some text.
def generate_itinerary(source, destination, start_date, end_date, no_of_day, budget):
    prompt = (
        f"Generate a personalized travel itinerary for a {no_of_day}-day trip "
        f"from {source} to {destination} on {start_date} to {end_date}, "
        f"with a budget of INR {budget}. Include low-cost accommodations and affordable activities "
        f"that match the budget."
    )
    response = model.generate_content(prompt)
    return response.text
