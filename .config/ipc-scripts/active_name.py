#!/usr/bin/python3
from wayfire import WayfireSocket
from wayfire.extra.ipc_utils import WayfireUtils
import time
import sys

# Initialize Wayfire socket and utility
sock = WayfireSocket()
utils = WayfireUtils(sock)

# Define the workspace mapping with your specific names
workspace_map = {
    (0, 0): "Home",
    (1, 0): "Web",
    (2, 0): "Editor",
    (0, 1): "Settings",
    (1, 1): "Second Web",
    (2, 1): "Slideshow",
    (0, 2): "System monitor",
    (1, 2): "Discord",
    (2, 2): "Media",
}

def get_ws_name():
    try:
        active_workspace = utils.get_active_workspace()
        x, y = active_workspace['x'], active_workspace['y']
        return workspace_map.get((x, y), "Unknown")
    except Exception:
        return "Wayfire Error"

# Initial output
last_ws = get_ws_name()
print(last_ws)
sys.stdout.flush()

# Continuous loop for Ironbar "watch" mode
while True:
    current_ws = get_ws_name()
    if current_ws != last_ws:
        print(current_ws)
        sys.stdout.flush() 
        last_ws = current_ws
    time.sleep(0.1)