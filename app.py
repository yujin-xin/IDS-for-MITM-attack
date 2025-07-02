import argparse
import subprocess
import re
import platform
import time
import datetime

def get_mac(ip):
    try:
        # Ping first to populate ARP table
        if platform.system() == "Windows":
            subprocess.run(['ping', '-n', '1', ip], capture_output=True)
            result = subprocess.run(['arp', '-a', ip], capture_output=True, text=True)
        else:
            subprocess.run(['ping', '-c', '1', ip], capture_output=True)
            result = subprocess.run(['arp', '-n', ip], capture_output=True, text=True)
        
        # Extract MAC address
        mac_pattern = r'([0-9a-fA-F]{2}[:-]){5}([0-9a-fA-F]{2})'
        match = re.search(mac_pattern, result.stdout)
        
        return match.group(0).replace('-', ':').lower() if match else None
    except:
        return None

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-g', required=True, help='IP address')
    parser.add_argument('-i', required=True, help="interval in seconds")
    args = parser.parse_args()

    td = datetime.datetime.now()

    with open("log.txt", "a") as f:
        f.write("---------------------------------------\n")
        f.write(f"Started @ {td}\n")
        f.write("---------------------------------------\n")

    while 1:
        mac = get_mac(args.g)

        with open("log.txt", "a") as f:
            td = datetime.datetime.now()
            f.write(f"{td} | {args.g} @ {mac}\n")
        
        time.sleep(int(args.i))

if __name__ == "__main__":
    main()