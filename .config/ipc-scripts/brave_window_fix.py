#!/usr/bin/python3

import os
import sys
import time
from wayfire import WayfireSocket
from wayfire.extra.ipc_utils import WayfireUtils

APP_ID = "brave-browser"
WORKSPACE_GRID_WIDTH = 3

sock = WayfireSocket()
utils = WayfireUtils(sock)
sock.watch(['view-mapped', 'view-geometry-changed'])

def force_resize(sock, view):
    current_x = view["geometry"]["x"]
    current_y = view["geometry"]["y"]
    current_width = view["geometry"]["width"]
    current_height = view["geometry"]["height"]

    #  Check if window is fullscreen
    is_fullscreen = utils.get_view_fullscreen(view["id"])
    if is_fullscreen:
        print(f"[{os.getpid()}] Brave window is in fullscreen mode, skipping resize.")
        return # Do not resize if it's fullscreen
  

    TARGET_X = 236
    TARGET_Y = 51
    TARGET_WIDTH = 1990
    TARGET_HEIGHT = 1232

    if current_x != TARGET_X or current_y != TARGET_Y or current_width != TARGET_WIDTH or current_height != TARGET_HEIGHT:
        print(f"[{os.getpid()}] Brave window resized to {current_x},{current_y} {current_width}x{current_height}. Forcing back to {TARGET_X},{TARGET_Y} {TARGET_WIDTH}x{TARGET_HEIGHT}.")
        sock.configure_view(view["id"], TARGET_X, TARGET_Y, TARGET_WIDTH, TARGET_HEIGHT)

def handle_event(event):

    if "event" not in event:
        return

    if event["event"] != "view-mapped" and event["event"] != "view-geometry-changed":
        return

    view = event["view"]
    if view.get("app-id") != APP_ID:
        return

    try:
        active_ws_coords = utils.get_active_workspace()
        active_workspace_index = active_ws_coords['y'] * WORKSPACE_GRID_WIDTH + active_ws_coords['x']
    except Exception as e:
        print(f"[{os.getpid()}] Could not get active workspace: {e}")
        return

    view_workspace = view.get('wset-index')

    if view_workspace is None:
        views = sock.list_views()
        for v in views:
            if v.get('id') == view.get('id'):
                view_workspace = v.get('wset-index')
                break

    if view_workspace == active_workspace_index:
        force_resize(sock, view)

while True:
    try:
        event = sock.read_next_event()
        if event:
            handle_event(event)
    except KeyboardInterrupt:
        print(f"[{os.getpid()}] Script terminated by KeyboardInterrupt.")
        break
    except Exception as e:
        print(f"[{os.getpid()}] An error occurred: {e}")
        break
