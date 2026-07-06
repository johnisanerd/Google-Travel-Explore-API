# ✈️ Google Travel Explore API: destination discovery as clean JSON

> The most efficient, reliable, and developer-friendly way to use the Google Travel Explore API.

**Actor page:** [apify.com/johnvc/google-travel-explore-api](https://apify.com/johnvc/google-travel-explore-api?fpr=9n7kx3)
**Input schema:** [apify.com/johnvc/google-travel-explore-api/input-schema](https://apify.com/johnvc/google-travel-explore-api/input-schema?fpr=9n7kx3)

Discover where you can travel from any airport and get destination ideas with prices and dates as structured JSON. For one or more departure airports, this API returns a ranked list of destinations, each with an estimated round-trip flight price, nightly hotel price, suggested trip dates, flight duration, number of stops, and a link. It is the missing piece for travel content sites, agencies, and AI travel agents.

## Video Walkthrough

[![Watch the walkthrough](https://img.youtube.com/vi/jREWahDGhJM/maxresdefault.jpg)](https://www.youtube.com/watch?v=jREWahDGhJM)

## Quick Start

### Prerequisites
- Python 3.11 or higher
- An Apify account and API key ([get a free key here](https://apify.com?fpr=9n7kx3))

1. **Clone the repository**
   ```bash
   git clone https://github.com/johnisanerd/Google-Travel-Explore-API.git
   cd Google-Travel-Explore-API
   ```

2. **Install dependencies with UV**
   ```bash
   # Install UV if you do not have it:
   curl -LsSf https://astral.sh/uv/install.sh | sh

   # Install project dependencies:
   uv sync
   ```

3. **Configure your API key**
   ```bash
   cp .env.example .env
   # Edit .env and add your Apify API key
   # Get your free API key at: https://apify.com?fpr=9n7kx3
   ```

4. **Run an example**
   ```bash
   # Single example:
   uv run python google-travel-explore-api-example.py

   # Batch example (explores from several airports in one run):
   uv run python google-travel-explore-api-batch-example.py
   ```

### Alternative: set the API key directly
```bash
export APIFY_API_TOKEN="your_api_key_here"
uv run python google-travel-explore-api-example.py
```

## Why Use This Google Travel Explore API?

One call, many priced destinations. Give it a departure airport and get a ranked list of places to go, each with flight and hotel prices and suggested dates.

Clean, structured output. Every destination is one row with a stable set of fields, ready to load into a dataframe, a database, or an AI travel agent.

Built for batch work. Pass several departure airports and compare reachable destinations and prices across them in one run.

MCP-ready. AI agents can call it as a tool through the hosted Apify MCP server, so an assistant can answer "where can I go for under $400 from JFK?"

## Features

### Core Capabilities
- Destination ideas from one or many departure airports
- Estimated round-trip flight price and nightly hotel price per destination
- Suggested trip dates, flight duration, and number of stops
- Localized pricing by country and language

### Data Quality
- One clean row per destination, ranked by relevance
- GPS coordinates and arrival airport details included
- Stable JSON shape, easy to load anywhere

## Usage Examples

### Basic Example
```json
{
  "departureId": "JFK",
  "maxResultsPerDeparture": 25
}
```

### Advanced Example
```json
{
  "departureIds": ["JFK", "SFO"],
  "gl": "us",
  "hl": "en",
  "maxResultsPerDeparture": 50
}
```

For a runnable batch script, see `google-travel-explore-api-batch-example.py` in this repo.

## Input Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `departureId` | `str` | one of | - | A single departure airport code, e.g. `JFK`, `LAX`, `LHR`. |
| `departureIds` | `list[str]` | one of | - | A batch of departure airport codes. Merged with `departureId` and de-duplicated. |
| `gl` | `str` | no | `"us"` | Two-letter country code for pricing and localization. |
| `hl` | `str` | no | `"en"` | Two-letter language code. |
| `maxResultsPerDeparture` | `int` | no | `50` | Destinations per departure airport (maximum 200). |

## Output Format

Each item in the dataset is one destination:

```json
{
  "result_type": "destination",
  "departure_id": "JFK",
  "position": 1,
  "name": "Los Angeles",
  "country": "United States",
  "destination_airport": { "code": "LAX", "location": "Los Angeles" },
  "gps_coordinates": { "latitude": 34.0549, "longitude": -118.2426 },
  "flight_price": 318,
  "hotel_price": 199,
  "flight_duration": 350,
  "number_of_stops": 0,
  "airline": "American and JetBlue",
  "airline_code": "multi",
  "start_date": "2026-06-21",
  "end_date": "2026-06-30",
  "link": "https://www.google.com/travel/explore?..."
}
```

---

<!-- The five install sections below are the canonical MCP install copy. -->

## Install in Claude Cowork Desktop

![Install in Claude Cowork Desktop](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_claude_desktop.png)

Cowork is the desktop app's automation mode. To give it the Google Travel Explore API as a tool, add the Apify MCP server as a connector.

1. Open the Claude desktop app and go to **Settings → Connectors** (or **Settings → Developer → Edit Config** to edit `claude_desktop_config.json` directly).
   - macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - Windows: `%APPDATA%\Claude\claude_desktop_config.json`
2. Add the Apify MCP server, preloaded with only this Actor:

```json
{
  "mcpServers": {
    "apify": {
      "command": "npx",
      "args": [
        "-y",
        "mcp-remote",
        "https://mcp.apify.com/?tools=actors,docs,johnvc/google-travel-explore-api"
      ]
    }
  }
}
```

3. Restart the app. When Cowork first calls the tool, complete the OAuth prompt in your browser, or add your Apify API token in the connector settings to skip OAuth.
4. In a Cowork chat, confirm the tool is available and ask it to run the Google Travel Explore API.

Download the desktop app and start a free trial: https://claude.ai/referral/uIlpa7nPLg
More help: https://docs.apify.com/platform/integrations/claude-desktop

---

## Install in Claude Code

![Install in Claude Code](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_claude_code.png)

Claude Code is the command-line tool. Add the Actor's MCP server with one command:

```bash
claude mcp add --transport http apify \
  "https://mcp.apify.com/?tools=actors,docs,johnvc/google-travel-explore-api"
```

To use a token instead of browser OAuth:

```bash
claude mcp add --transport http apify \
  "https://mcp.apify.com/?tools=actors,docs,johnvc/google-travel-explore-api" \
  --header "Authorization: Bearer YOUR_APIFY_TOKEN"
```

Then verify with `claude mcp list`, or run `/mcp` inside a session. Ask Claude Code to call the Google Travel Explore API.

Try Claude Code free: https://claude.ai/referral/uIlpa7nPLg
Claude Code MCP docs: https://code.claude.com/docs/en/mcp

---

## Install in Claude (website)

![Install in Claude (website)](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_claude_ai.png)

On claude.ai you add Apify as a connector, then enable just this Actor's tool.

1. Go to **Settings → Connectors → Browse connectors** and search for **Apify MCP server**. Install it (enable or update if prompted).
2. When connecting, authenticate with your Apify API token, and enable the tool `johnvc/google-travel-explore-api`.
3. In any chat, open **+ → Connectors** and turn on **Apify**.
4. Alternatively, choose **Add custom connector** and paste the full MCP URL `https://mcp.apify.com/?tools=actors,docs,johnvc/google-travel-explore-api`, using OAuth when prompted.
5. Ask Claude to run the Google Travel Explore API.

Open Claude on the web: https://claude.ai

---

## Install in Cursor

![Install in Cursor](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_cursor.png)

Cursor reads MCP servers from a project file at `.cursor/mcp.json`.

1. In your project, create `.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "apify": {
      "url": "https://mcp.apify.com/?tools=actors,docs,johnvc/google-travel-explore-api"
    }
  }
}
```

2. If you prefer token auth over browser OAuth, add a header:

```json
{
  "mcpServers": {
    "apify": {
      "url": "https://mcp.apify.com/?tools=actors,docs,johnvc/google-travel-explore-api",
      "headers": { "Authorization": "Bearer YOUR_APIFY_TOKEN" }
    }
  }
}
```

3. Open **Cursor → Settings → MCP** and confirm the **apify** server is connected (green dot).
4. In Composer or Chat, ask Cursor to call the Google Travel Explore API.

New to Cursor? Get it here: https://cursor.com/referral?code=XQP4VBLI3NNX

---

## Install in ChatGPT

![Install in ChatGPT](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_ChatGPT.png)

ChatGPT connects to the Apify MCP server through Developer mode (available on ChatGPT Pro, Plus, Business, Enterprise, and Education plans).

1. Click your profile icon, then go to **Settings > Apps**. If you do not see a **Create app** button, open **Advanced settings** and enable **Developer mode**.
2. Click **Create app** and fill out the form:
   - **Name:** Apify
   - **MCP Server URL:** `https://mcp.apify.com/?tools=actors,docs,johnvc/google-travel-explore-api`
   - **Authentication:** OAuth
3. Click **Create** and authorize the connection with Apify.
4. To use the app in a conversation, click **+** in the chat, choose **Developer mode**, and select **Apify**.

More help: https://docs.apify.com/platform/integrations/mcp

---

[**Made with care**](https://apify.com/johnvc?fpr=9n7kx3)

*Use the Google Travel Explore API to power destination discovery for your travel product or AI agent.*

## Featured Tasks

Ready-to-run examples on the Apify Store, each targeting one departure city:

- [Cheapest Places to Fly From New York With Prices](https://apify.com/johnvc/google-travel-explore-api/examples/cheapest-places-to-fly-from-new-york-with-prices?fpr=9n7kx3)
- [Cheapest Places to Fly From Los Angeles With Prices](https://apify.com/johnvc/google-travel-explore-api/examples/cheapest-places-to-fly-from-los-angeles-with-prices?fpr=9n7kx3)
- [Cheapest Places to Fly From Chicago With Prices](https://apify.com/johnvc/google-travel-explore-api/examples/cheapest-places-to-fly-from-chicago-with-prices?fpr=9n7kx3)
- [Cheapest Places to Fly From Atlanta With Prices](https://apify.com/johnvc/google-travel-explore-api/examples/cheapest-places-to-fly-from-atlanta-with-prices?fpr=9n7kx3)
- [Cheapest Places to Fly From Boston With Prices](https://apify.com/johnvc/google-travel-explore-api/examples/cheapest-places-to-fly-from-boston-with-prices?fpr=9n7kx3)
- [Cheapest Places to Fly From San Francisco With Prices](https://apify.com/johnvc/google-travel-explore-api/examples/cheapest-places-to-fly-from-san-francisco-with-prices?fpr=9n7kx3)
- [Cheapest Places to Fly From Miami With Prices](https://apify.com/johnvc/google-travel-explore-api/examples/cheapest-places-to-fly-from-miami-with-prices?fpr=9n7kx3)
- [Cheapest Places to Fly From Seattle With Prices](https://apify.com/johnvc/google-travel-explore-api/examples/cheapest-places-to-fly-from-seattle-with-prices?fpr=9n7kx3)
- [Cheapest Places to Fly From Dallas With Prices](https://apify.com/johnvc/google-travel-explore-api/examples/cheapest-places-to-fly-from-dallas-with-prices?fpr=9n7kx3)
- [Cheapest Places to Fly From Denver With Prices](https://apify.com/johnvc/google-travel-explore-api/examples/cheapest-places-to-fly-from-denver-with-prices?fpr=9n7kx3)
- [Export Travel Destinations to CSV](https://apify.com/johnvc/google-travel-explore-api/examples/export-travel-destinations-to-csv?fpr=9n7kx3)

Last Updated: 2026.07.06
