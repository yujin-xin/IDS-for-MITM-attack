# IDS-for-MITM-attack
This is a bare minimum Host-based IDS specifically for Man-in-the-Middle attack.

What it does is constantly monitoring the physical address of the gateway and logging it into log.txt
When an anomaly happens―such as your current device is under eavesdrop―, it creates a new text file (anomaly.txt) to log the current event.

run:
python app.py -g *your LAN's gateway address* -i *interval*

ps: this project is under development. Planning to create a centralized server for monitoring in the feature