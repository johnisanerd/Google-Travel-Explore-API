"""
Google Travel Explore API: A Quick Start Example
See more at: https://apify.com/johnvc/google-travel-explore-api?fpr=9n7kx3
Input schema: https://apify.com/johnvc/google-travel-explore-api/input-schema?fpr=9n7kx3

This script shows how to call the Google Travel Explore API on Apify from Python
and read its structured JSON output. It returns destination ideas from a
departure airport, with flight and hotel prices. Inputs are kept small so your
first call stays cheap.

Get your free Apify API key at: https://apify.com?fpr=9n7kx3
"""

import os
from dotenv import load_dotenv
from apify_client import ApifyClient

load_dotenv()

# Initialize the Apify client with your API token (read from .env)
client = ApifyClient(os.getenv("APIFY_API_TOKEN"))

# Build the Actor input.
# Inputs are kept small (one departure airport, 10 destinations) to keep this
# first run inexpensive: you are billed per destination returned.
run_input = {
    "departureId": "JFK",          # the airport you are flying from
    "gl": "us",                    # country for pricing/localization
    "hl": "en",                    # interface language
    "maxResultsPerDeparture": 10,  # small on purpose to keep it cheap
}

# Run the Actor and wait for it to finish
run = client.actor("johnvc/google-travel-explore-api").call(run_input=run_input)
if run is None:
    raise SystemExit("The Actor run did not return a result.")

# Read structured results from the run's default dataset
# (apify-client 3.x returns a Run object; use .default_dataset_id, not run["..."])
items = list(client.dataset(run.default_dataset_id).iterate_items())
print(f"Returned {len(items)} destination(s).\n")

# Show each destination with its prices and dates.
for item in items:
    name = item.get("name", "")
    country = item.get("country", "")
    flight = item.get("flight_price")
    hotel = item.get("hotel_price")
    start = item.get("start_date", "")
    end = item.get("end_date", "")
    print(f"{item.get('position')}. {name}, {country}")
    print(f"   flight ~${flight}, hotel ~${hotel}/night, {start} to {end}\n")
