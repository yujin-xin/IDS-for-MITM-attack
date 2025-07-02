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

    initial_mac = get_mac(args.g)
    print("IDS running...")
    print(f"Gateway's mac: {initial_mac}")
    
    with open("log.txt", "a") as f:
        f.write("---------------------------------------\n")
        f.write(f"Started @ {td}\n")
        f.write("---------------------------------------\n")

    anomaly_tracker = True
    while 1:
        current_mac = get_mac(args.g)
        td = datetime.datetime.now()   

        #log's the entire operation (mac base for now)
        with open("log.txt", "a") as f:
            f.write(f"{td} | {args.g} @ {current_mac}\n")
        
        # create anomaly.txt and logs it
        if current_mac != initial_mac:
            if anomaly_tracker:
                print(f"Gateway's mac address has been change to: {current_mac}")
                
                with open("anomaly.txt", "a") as f:
                    f.write("---------------------------------------\n")
                    f.write(f"Anomaly started @ {td}\n")
                    f.write("---------------------------------------\n")
                
                anomaly_tracker = False

            with open("anomaly.txt", "a") as f:
                f.write(f"{td} | {args.g} @ {current_mac}\n")
        else:
            anomaly_tracker = True


        time.sleep(int(args.i))



if __name__ == "__main__":
    main()