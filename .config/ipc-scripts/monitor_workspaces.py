#!/usr/bin/python3
import subprocess
import time
from wayfire import WayfireSocket
from wayfire.extra.ipc_utils import WayfireUtils

# Global variable to track the previously highlighted workspace
last_active_num = None

def update_ironbar(active_num):
    global last_active_num
    
    # 1. If this is the first run, clear all workspaces once to be safe
    if last_active_num is None:
        for i in range(1, 10):
            subprocess.run(["ironbar", "style", "remove-class", f"work{i}", "active"], capture_output=True)
    
    # 2. Remove the 'active' class from the previous workspace only
    elif last_active_num != active_num:
        subprocess.run(["ironbar", "style", "remove-class", f"work{last_active_num}", "active"], capture_output=True)
    
    # 3. Add the 'active' class to the new current workspace
    subprocess.run(["ironbar", "style", "add-class", f"work{active_num}", "active"], capture_output=True)
    
    # Update the tracker
    last_active_num = active_num

try:
    sock = WayfireSocket()
    utils = WayfireUtils(sock)
except Exception:
    exit(1)

# Mapping coordinates to workspace numbers
workspace_map = {
    (0,0):1, (1,0):2, (2,0):3, 
    (0,1):4, (1,1):5, (2,1):6, 
    (0,2):7, (1,2):8, (2,2):9
}

last_ws = None

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
