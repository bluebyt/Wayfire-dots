#!/usr/bin/python3

import subprocess
import os
import time
from wayfire import WayfireSocket

# 1. CONNECT AND WATCH FIRST
sock = WayfireSocket()
sock.watch(['view-mapped'])
print("Socket connected. Listening for new windows...")

# 2. LAUNCH THE PROCESSES
subprocess.Popen(["thunar", os.path.expanduser("~")])
time.sleep(1)
subprocess.Popen(["thunar", os.path.expanduser("~/Downloads/")])
time.sleep(1)
subprocess.Popen(["thunar", os.path.expanduser("/mnt/media/")])
print("Thunar processes launched.")

# 3. PROCESS EVENTS IN A LOOP
print("Entering event loop. Waiting for windows...")
while True:
    try:
        msg = sock.read_next_event()
        if not (msg and "event" in msg and msg["event"] == "view-mapped"):
            continue

        view = msg["view"]
        title = view.get("title", "")
        print(f"\n--- Caught New Window ---\n    Title: {title}")

        # YOUR RULES ARE HERE, INSIDE THE LOOP
        if title == "bluebyt - Thunar":
            print("    MATCHED: 'bluebyt - Thunar'. Applying rule...")
            sock.configure_view(view["id"], 285, 83, 733, 536)
            sock.set_workspace(0, 0, view["id"])

        elif title == "Downloads - Thunar":
            print("    MATCHED: 'Downloads - Thunar'. Applying rule...")
            sock.configure_view(view["id"], 285, 83, 733, 536)
            sock.set_workspace(2, 0, view["id"])

        elif title == "media - Thunar":
            print("    MATCHED: 'media - Thunar'. Applying rule...")
            sock.configure_view(view["id"], 285, 83, 733, 536)
            sock.set_workspace(2, 2, view["id"])
        
        # THIS WILL TELL US IF THE TITLE IS UNEXPECTED
        else:
            print(f"    NO MATCH: The title '{title}' did not match any of your rules.")
            print(f"    (App-ID was: {view.get('app-id')})")

    except KeyboardInterrupt:
        break
    except Exception as e:
        print(f"An error occurred: {e}")

print("\nScript finished.")
