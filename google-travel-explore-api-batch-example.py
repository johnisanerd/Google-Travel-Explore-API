"""
Google Travel Explore API: Batch Multi-Departure Example
See more at: https://apify.com/johnvc/google-travel-explore-api?fpr=9n7kx3
Input schema: https://apify.com/johnvc/google-travel-explore-api/input-schema?fpr=9n7kx3

This script shows the batch capability of the Google Travel Explore API on
Apify: pass a list of departure airport codes with the `departureIds` input and
the Actor pulls destination ideas for each in a single run, tagging every
destination with its `departure_id`. That makes it easy to compare what is
reachable, and at what price, from several home airports. Inputs are kept small
so your first call stays cheap.

Get your free Apify API key at: https://apify.com?fpr=9n7kx3
"""

import os
from collections import defaultdict
from dotenv import load_dotenv
from apify_client import ApifyClient

load_dotenv()

# Initialize the Apify client with your API token (read from .env)
client = ApifyClient(os.getenv("APIFY_API_TOKEN"))

# Build the Actor input.
# This run uses the `departureIds` list to explore from several airports at
# once. Each destination row carries the `departure_id` it came from.
# maxResultsPerDeparture is kept small (10) to keep this first run inexpensive:
# you are billed per destination returned. Raise it or add airports once you
# know your budget.
run_input = {
    "departureIds": ["JFK", "SFO"],  # the airports you are flying from
    "gl": "us",                      # country for pricing/localization
    "hl": "en",                      # interface language
    "maxResultsPerDeparture": 10,    # small on purpose to keep it cheap
}

# Run the Actor and wait for it to finish
run = client.actor("johnvc/google-travel-explore-api").call(run_input=run_input)
if run is None:
    raise SystemExit("The Actor run did not return a result.")

# Read structured results from the run's default dataset
# (apify-client 3.x returns a Run object; use .default_dataset_id, not run["..."])
items = list(client.dataset(run.default_dataset_id).iterate_items())
print(f"Returned {len(items)} destination(s) across {len(run_input['departureIds'])} airport(s).\n")

# Group the destinations by their departure airport so the batch structure is visible.
by_departure = defaultdict(list)
for item in items:
    by_departure[item.get("departure_id", "")].append(item)

# Print a short report per departure airport.
for departure_id in run_input["departureIds"]:
    destinations = by_departure.get(departure_id, [])
    print(f"=== From {departure_id}: {len(destinations)} destination(s) ===")
    for item in destinations:
        name = item.get("name", "")
        country = item.get("country", "")
        flight = item.get("flight_price")
        hotel = item.get("hotel_price")
        print(f"  {item.get('position')}. {name}, {country}: flight ~${flight}, hotel ~${hotel}/night")
    print()
