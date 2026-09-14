import json
from datetime import datetime, timedelta
from pathlib import Path


# --------------------------------------------------
# SETTINGS
# --------------------------------------------------

INPUT_FILE = Path("data/contributions.json")
OUTPUT_FILE = Path("assets/activity-dashboard.svg")

WIDTH = 1000
HEIGHT = 500


# --------------------------------------------------
# LOAD CONTRIBUTION DATA
# --------------------------------------------------

print("Loading contribution data...")

with open(INPUT_FILE, "r", encoding="utf-8") as file:
    data = json.load(file)

contributions = data["contributions"]


# --------------------------------------------------
# CALCULATE BASIC STATISTICS
# --------------------------------------------------

total_activity = sum(contributions.values())

active_days = sum(
    1 for value in contributions.values()
    if value > 0
)


# --------------------------------------------------
# CALCULATE CURRENT STREAK
# --------------------------------------------------

dates = sorted(
    contributions.keys(),
    reverse=True
)

current_streak = 0

today = datetime.utcnow().date()

for date_string in dates:

    date = datetime.strptime(
        date_string,
        "%Y-%m-%d"
    ).date()

    if date > today:
        continue

    if contributions[date_string] > 0:

        current_streak += 1

    else:

        break


# --------------------------------------------------
# CALCULATE LONGEST STREAK
# --------------------------------------------------

sorted_dates = sorted(contributions.keys())

longest_streak = 0
streak = 0
previous_date = None

for date_string in sorted_dates:

    date = datetime.strptime(
        date_string,
        "%Y-%m-%d"
    ).date()

    if contributions[date_string] > 0:

        if (
            previous_date is not None
            and date == previous_date + timedelta(days=1)
        ):

            streak += 1

        else:

            streak = 1

        longest_streak = max(
            longest_streak,
            streak
        )

    else:

        streak = 0

    previous_date = date


# --------------------------------------------------
# HEATMAP
# --------------------------------------------------

recent_dates = sorted(
    contributions.keys()
)[-364:]


cell_size = 13
gap = 3

start_x = 40
start_y = 145


heatmap = ""

for index, date_string in enumerate(recent_dates):

    value = contributions[date_string]

    row = index % 7
    column = index // 7

    x = start_x + column * (cell_size + gap)
    y = start_y + row * (cell_size + gap)

    # Different intensity levels
    if value == 0:
        opacity = "0.10"
    elif value == 1:
        opacity = "0.30"
    elif value == 2:
        opacity = "0.50"
    elif value == 3:
        opacity = "0.70"
    else:
        opacity = "1.0"

    heatmap += f"""
    <rect
        x="{x}"
        y="{y}"
        width="{cell_size}"
        height="{cell_size}"
        rx="3"
        fill="#00ff9d"
        fill-opacity="{opacity}">
    </rect>
    """


# --------------------------------------------------
# CREATE SVG
# --------------------------------------------------

svg = f"""<svg
xmlns="http://www.w3.org/2000/svg"
width="{WIDTH}"
height="{HEIGHT}"
viewBox="0 0 {WIDTH} {HEIGHT}">

<defs>

    <filter id="glow">

        <feGaussianBlur
            stdDeviation="3"
            result="coloredBlur"/>

        <feMerge>

            <feMergeNode in="coloredBlur"/>
            <feMergeNode in="SourceGraphic"/>

        </feMerge>

    </filter>

</defs>


<!-- BACKGROUND -->

<rect
    width="100%"
    height="100%"
    rx="20"
    fill="#050b0d"/>


<!-- BORDER -->

<rect
    x="1"
    y="1"
    width="{WIDTH - 2}"
    height="{HEIGHT - 2}"
    rx="20"
    fill="none"
    stroke="#00ff9d"
    stroke-opacity="0.35"/>


<!-- TITLE -->

<text
    x="40"
    y="50"
    fill="#00ff9d"
    font-family="monospace"
    font-size="24"
    font-weight="bold">

    GITHUB_ACTIVITY

</text>


<text
    x="40"
    y="80"
    fill="#8ca3a8"
    font-family="monospace"
    font-size="14">

    github.com/shreyashhtiwarii

</text>


<!-- STATUS -->

<circle
    cx="935"
    cy="45"
    r="6"
    fill="#00ff9d"
    filter="url(#glow)"/>


<text
    x="950"
    y="50"
    fill="#00ff9d"
    font-family="monospace"
    font-size="13">

    ACTIVE

</text>


<!-- HEATMAP -->

<text
    x="40"
    y="120"
    fill="#ffffff"
    font-family="monospace"
    font-size="15">

    CONTRIBUTION HEATMAP

</text>

{heatmap}


<!-- STAT BOXES -->

<rect
    x="40"
    y="300"
    width="210"
    height="110"
    rx="12"
    fill="#081316"
    stroke="#00ff9d"
    stroke-opacity="0.25"/>


<rect
    x="270"
    y="300"
    width="210"
    height="110"
    rx="12"
    fill="#081316"
    stroke="#00ff9d"
    stroke-opacity="0.25"/>


<rect
    x="500"
    y="300"
    width="210"
    height="110"
    rx="12"
    fill="#081316"
    stroke="#00ff9d"
    stroke-opacity="0.25"/>


<rect
    x="730"
    y="300"
    width="210"
    height="110"
    rx="12"
    fill="#081316"
    stroke="#00ff9d"
    stroke-opacity="0.25"/>


<!-- STAT 1 -->

<text
    x="60"
    y="335"
    fill="#8ca3a8"
    font-family="monospace"
    font-size="13">

    ACTIVITY

</text>


<text
    x="60"
    y="375"
    fill="#00ff9d"
    font-family="monospace"
    font-size="28"
    font-weight="bold">

    {total_activity}

</text>


<!-- STAT 2 -->

<text
    x="290"
    y="335"
    fill="#8ca3a8"
    font-family="monospace"
    font-size="13">

    ACTIVE DAYS

</text>


<text
    x="290"
    y="375"
    fill="#00ff9d"
    font-family="monospace"
    font-size="28"
    font-weight="bold">

    {active_days}

</text>


<!-- STAT 3 -->

<text
    x="520"
    y="335"
    fill="#8ca3a8"
    font-family="monospace"
    font-size="13">

    CURRENT STREAK

</text>


<text
    x="520"
    y="375"
    fill="#00ff9d"
    font-family="monospace"
    font-size="28"
    font-weight="bold">

    {current_streak}

</text>


<!-- STAT 4 -->

<text
    x="750"
    y="335"
    fill="#8ca3a8"
    font-family="monospace"
    font-size="13">

    LONGEST STREAK

</text>


<text
    x="750"
    y="375"
    fill="#00ff9d"
    font-family="monospace"
    font-size="28"
    font-weight="bold">

    {longest_streak}

</text>


<!-- FOOTER -->

<text
    x="40"
    y="455"
    fill="#53676d"
    font-family="monospace"
    font-size="12">

    AI / ML • DATA ANALYTICS • CYBERSECURITY • CLOUD

</text>


<text
    x="40"
    y="478"
    fill="#53676d"
    font-family="monospace"
    font-size="11">

    AUTO-GENERATED • SHREYASH TIWARI

</text>


</svg>
"""


# --------------------------------------------------
# SAVE SVG
# --------------------------------------------------

OUTPUT_FILE.parent.mkdir(
    parents=True,
    exist_ok=True
)

with open(
    OUTPUT_FILE,
    "w",
    encoding="utf-8"
) as file:

    file.write(svg)


print("Dashboard created successfully!")
print(f"Output: {OUTPUT_FILE}")