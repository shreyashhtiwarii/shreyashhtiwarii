from pathlib import Path

output = Path("assets/terminal-header.svg")

svg = '''<svg xmlns="http://www.w3.org/2000/svg"
width="1000"
height="430"
viewBox="0 0 1000 430">

<style>

.terminal {
    font-family: monospace;
    fill: #d7fff0;
}

.green {
    fill: #00ff9c;
}

.cyan {
    fill: #00d9ff;
}

.line {
    opacity: 0;
    animation: appear 0.7s ease forwards;
}

.line1 { animation-delay: 0.5s; }
.line2 { animation-delay: 1.1s; }
.line3 { animation-delay: 1.7s; }
.line4 { animation-delay: 2.3s; }
.line5 { animation-delay: 2.9s; }
.line6 { animation-delay: 3.5s; }

@keyframes appear {

    from {
        opacity: 0;
        transform: translateX(-15px);
    }

    to {
        opacity: 1;
        transform: translateX(0);
    }

}

.cursor {
    animation: blink 1s steps(2) infinite;
}

@keyframes blink {
    50% {
        opacity: 0;
    }
}

</style>


<!-- Terminal -->

<rect
x="5"
y="5"
width="990"
height="420"
rx="18"
fill="#080d0c"
stroke="#1d4038"
stroke-width="2"/>


<!-- Header -->

<rect
x="5"
y="5"
width="990"
height="55"
rx="18"
fill="#101917"/>


<!-- Mac-style buttons -->

<circle cx="35" cy="32" r="8" fill="#ff5f56"/>
<circle cx="62" cy="32" r="8" fill="#ffbd2e"/>
<circle cx="89" cy="32" r="8" fill="#27c93f"/>


<text
x="125"
y="39"
class="terminal muted"
font-size="18">

shreyash@github: ~

</text>


<!-- Content -->

<text
x="45"
y="110"
class="terminal green line line1"
font-size="21">

$ whoami

</text>


<text
x="45"
y="155"
class="terminal line line2"
font-size="32"
font-weight="bold">

SHREYASH TIWARI

</text>


<text
x="45"
y="190"
class="terminal cyan line line3"
font-size="20">

BTech Artificial Intelligence Student

</text>


<text
x="45"
y="235"
class="terminal green line line4"
font-size="20">

AI / ML • DATA ANALYTICS • CYBERSECURITY • CLOUD

</text>


<text
x="45"
y="280"
class="terminal green line line5"
font-size="20">

$ ./status.sh

</text>


<text
x="45"
y="320"
class="terminal line line6"
font-size="19">

● Building intelligent systems

</text>


<text
x="45"
y="350"
class="terminal line line6"
font-size="19">

● Exploring Machine Learning &amp; Data Analytics

</text>


<text
x="45"
y="380"
class="terminal line line6"
font-size="19">

● Learning AWS &amp; Cloud Computing

</text>


<text
x="45"
y="407"
class="terminal green cursor"
font-size="18">

█

</text>

</svg>
'''

output.parent.mkdir(parents=True, exist_ok=True)

output.write_text(svg, encoding="utf-8")

print("Terminal SVG created successfully!")