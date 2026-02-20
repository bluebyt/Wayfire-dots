#!/usr/bin/python3

import html
import json
import sys
from wayfire import WayfireSocket

def get_title():
    socket = WayfireSocket()
    focused_view = socket.get_focused_view()
    
    if focused_view and focused_view.get("title"):
        title = focused_view.get("title")
        # Crop and Escape
        cropped = title[:20] + "..." if len(title) > 20 else title
        return html.escape(cropped)
    return "No focused window"

def monitor_focus():
    socket = WayfireSocket()
    # Tell Wayfire we want to listen to view events
    socket.watch(['view-focused'])
    
    # Print the initial title
    print(get_title())
    sys.stdout.flush()

    while True:
        try:
            # Wait for an event from Wayfire
            msg = socket.read_message()
            if msg:
                # Every time focus changes, print the new title
                print(get_title())
                sys.stdout.flush()
        except Exception:
            break

if __name__ == "__main__":
    monitor_focus()
