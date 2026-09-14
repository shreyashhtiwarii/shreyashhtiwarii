import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime

USERNAME = "shreyashhtiwarii"

URL = f"https://github.com/users/{USERNAME}/contributions"

print("Fetching GitHub contribution data...")

try:
    response = requests.get(
        URL,
        headers={
            "User-Agent": "Mozilla/5.0"
        },
        timeout=20
    )

    response.raise_for_status()

except requests.RequestException as e:
    print("Error while connecting to GitHub:")
    print(e)
    exit(1)


soup = BeautifulSoup(response.text, "html.parser")

contributions = {}

cells = soup.select("td.ContributionCalendar-day")

print(f"Found {len(cells)} contribution cells.")


for cell in cells:

    date = cell.get("data-date")
    level = cell.get("data-level")

    if not date:
        continue

    try:
        level = int(level) if level is not None else 0
    except ValueError:
        level = 0

    contributions[date] = level


if not contributions:
    print("No contribution data found.")
    print("GitHub may have changed its contribution page structure.")
    exit(1)


output = {
    "username": USERNAME,
    "generated_at": datetime.utcnow().isoformat() + "Z",
    "contributions": contributions
}


with open(
    "data/contributions.json",
    "w",
    encoding="utf-8"
) as file:

    json.dump(
        output,
        file,
        indent=2
    )


print("Successfully saved contribution data.")

print(
    f"Total days collected: {len(contributions)}"
)

print(
    "File created: data/contributions.json"
)