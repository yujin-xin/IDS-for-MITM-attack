# Host-based ARP Poisoning Detection Logger – Python CLI (IDS)

## Overview
A Python-based, command-line Intrusion Detection tool focused on ARP poisoning detection within local area networks (LANs). The system monitors the MAC address associated with the default network gateway and logs any changes, helping to identify signs of Man-in-the-Middle (MitM) attacks.

## key Features
* Gateway MAC Monitoring: Continuously checks the MAC address of the network’s default gateway to detect unauthorized modifications.
* ARP Spoofing Detection: Helps identify common local attack (e.g., MitM via ARP poisoning, DNS poisoning).
* Passive Logging: Suspicious changes are logged to a local file for review.
* Lightweight CLI Tool: Runs from the command line with minimal system overhead, making it ideal for background operation on monitoring endpoints or internal hosts.

## Use Cases
* Providing evidence of ARP spoofing attempts during internal incident response
* Feeding into larger security monitoring pipelines or SIEM platforms
* Learning and demonstrating practical LAN-level threat detection in blue team workflows

## Benefits
* Serves as a practical entry point into network-based threat detection, with a clear focus on LAN-specific attack methods.
* Reinforces core SOC analyst skills such as passive detection, traffic analysis, and network baseline awareness.
* Easily extendable to support alerting mechanisms (e.g., syslog, email, or webhook integration) as part of future iterations.

## Technical Stack
* Networking: TCP/IP stack
* Language: Python
* Packet Analysis: scapy-based
* Logging: Plaintext logs saved locally
* Platform: Unix/Linux-based systems (root privileges required for packet access)
* Interface: Command-line

```bash
git clone https://github.com/yujin-xin/IDS-for-MITM-attack
cd IDS-for-MITM-attack
python app.py -g <your LAN's gateway address> -i <interval>
```

