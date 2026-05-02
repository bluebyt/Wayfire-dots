#!/usr/bin/python3
from wayfire import WayfireSocket
from wayfire.extra.ipc_utils import WayfireUtils
import time
import sys

# Initialize Wayfire socket and utility
sock = WayfireSocket()
utils = WayfireUtils(sock)

# Define the workspace mapping grid
workspace_map = {
    (0, 0): 1, (1, 0): 2, (2, 0): 3,
    (0, 1): 4, (1, 1): 5, (2, 1): 6,
    (0, 2): 7, (1, 2): 8, (2, 2): 9,
}

def get_ws():
    active_workspace = utils.get_active_workspace()
    x, y = active_workspace['x'], active_workspace['y']
    return workspace_map.get((x, y), "?")

# Initial print
last_ws = get_ws()
print(last_ws)
sys.stdout.flush()

# Loop to monitor changes
while True:
    current_ws = get_ws()
    if current_ws != last_ws:
        print(current_ws)
        sys.stdout.flush() # Forces Ironbar to see the update immediately
        last_ws = current_ws
    time.sleep(0.1) # Small delay to prevent high CPU usage