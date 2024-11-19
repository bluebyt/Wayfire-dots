#!/usr/bin/python3
from wayfire import WayfireSocket
from wayfire.extra.ipc_utils import WayfireUtils

# Initialize Wayfire socket and utility
sock = WayfireSocket()
utils = WayfireUtils(sock)

# Get the active workspace info
active_workspace = utils.get_active_workspace()

# Define the workspace mapping grid
workspace_map = {
    (0, 0): 1,
    (1, 0): 2,
    (2, 0): 3,
    (0, 1): 4,
    (1, 1): 5,
    (2, 1): 6,
    (0, 2): 7,
    (1, 2): 8,    
    (2, 2): 9,
}

# Get the x and y coordinates
x, y = active_workspace['x'], active_workspace['y']

# Find the corresponding workspace number
workspace_number = workspace_map.get((x, y), "Unknown workspace")

# Print the result
print(f"{workspace_number}")

