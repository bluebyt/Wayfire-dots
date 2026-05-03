#!/usr/bin/python3
import subprocess
import time
import os
from wayfire import WayfireSocket
from wayfire.extra.ipc_utils import WayfireUtils

# Absolute path to ironbar since it's in a local bin
IRONBAR_PATH = "/home/bluebyt/.local/bin/ironbar"

# Global variable to track the previously highlighted workspace
last_active_num = None

def force_initial_active(num):
    """
    Attempts to set the active class repeatedly until it sticks,
    ensuring we overcome Ironbar's slow widget initialization at boot.
    """
    success = False
    attempts = 0
    while not success and attempts < 15:
        res = subprocess.run([IRONBAR_PATH, "style", "add-class", f"work{num}", "active"], capture_output=True)
        time.sleep(0.5)
        # We consider it a success after a few successful hits to ensure the UI is stable
        if res.returncode == 0:
            attempts += 1 
        if attempts == 5:
            success = True

def update_ironbar(active_num):
    global last_active_num
    
    # 1. If this is the first run, clear all workspaces once to be safe
    if last_active_num is None:
        for i in range(1, 10):
            subprocess.run([IRONBAR_PATH, "style", "remove-class", f"work{i}", "active"], capture_output=True)
    
    # 2. Remove the 'active' class from the previous workspace only
    elif last_active_num != active_num:
        subprocess.run([IRONBAR_PATH, "style", "remove-class", f"work{last_active_num}", "active"], capture_output=True)
    
    # 3. Add the 'active' class to the new current workspace
    subprocess.run([IRONBAR_PATH, "style", "add-class", f"work{active_num}", "active"], capture_output=True)
    
    # Update the tracker
    last_active_num = active_num

# Wait for Wayfire socket to be ready
sock = None
utils = None
while sock is None:
    try:
        sock = WayfireSocket()
        utils = WayfireUtils(sock)
    except Exception:
        time.sleep(0.5)

# Mapping coordinates to workspace numbers
workspace_map = {
    (0,0):1, (1,0):2, (2,0):3, 
    (0,1):4, (1,1):5, (2,1):6, 
    (0,2):7, (1,2):8, (2,2):9
}

# Get initial workspace and force the highlight
ws = utils.get_active_workspace()
initial_num = workspace_map.get((ws['x'], ws['y']), 1)
force_initial_active(initial_num)
last_ws = initial_num
last_active_num = initial_num

while True:
    try:
        ws = utils.get_active_workspace()
        num = workspace_map.get((ws['x'], ws['y']), 0)

        # Only trigger the update if the workspace actually changed
        if num != last_ws and num != 0:
            update_ironbar(num)
            last_ws = num
            
    except Exception:
        # Re-establish socket if connection is lost
        try:
            sock = WayfireSocket()
            utils = WayfireUtils(sock)
        except:
            pass
            
    time.sleep(0.1)
