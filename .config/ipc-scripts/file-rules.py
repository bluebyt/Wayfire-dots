#!/usr/bin/python3

import subprocess
import os
import time
from wayfire import WayfireSocket

# 1. CONNECT AND WATCH
sock = WayfireSocket()
sock.watch(['view-mapped', 'view-title-changed'])
print("Socket connected. Listening for initial window setup...")

# 2. LAUNCH THE PROCESSES
subprocess.Popen(["nautilus", "-w", os.path.expanduser("~")])
time.sleep(1)
subprocess.Popen(["nautilus", "-w", os.path.expanduser("~/Downloads/")])
time.sleep(1)
subprocess.Popen(["nautilus", "-w", os.path.expanduser("/mnt/media/")])
print("Nautilus processes launched.")

# 3. PROCESS EVENTS UNTIL ALL WINDOWS ARE CONFIGURED
print("Entering event loop...")
configured_windows = set()

while True:
    try:
        # Exit if we've already configured the 3 windows
        if len(configured_windows) >= 3:
            print("\nAll 3 initial windows have been configured. Script finished.")
            break

        msg = sock.read_next_event()
        if not (msg and "event" in msg and msg["event"] == 'view-title-changed'):
            continue

        view = msg["view"]
        view_id = view.get("id")

        # If we have already handled this window, ignore future title changes
        if view_id in configured_windows:
            continue

        title = view.get("title", "")
        rule_matched = False

        if title == "Home":
            print(f"MATCHED: 'Home' (ID: {view_id}). Applying rule.")
            sock.configure_view(view_id, 285, 83, 733, 536)
            sock.set_workspace(0, 0, view_id)
            rule_matched = True

        elif title == "Downloads":
            print(f"MATCHED: 'Downloads' (ID: {view_id}). Applying rule.")
            sock.configure_view(view_id, 285, 83, 733, 536)
            sock.set_workspace(2, 0, view_id)
            rule_matched = True

        elif title == "media":
            print(f"MATCHED: 'media' (ID: {view_id}). Applying rule.")
            sock.configure_view(view_id, 285, 83, 733, 536)
            sock.set_workspace(2, 2, view_id)
            rule_matched = True
        
        # If a rule was applied, add the window ID to our set
        if rule_matched:
            configured_windows.add(view_id)

    except KeyboardInterrupt:
        break
    except Exception as e:
        print(f"An error occurred: {e}")
