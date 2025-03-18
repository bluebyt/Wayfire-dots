#!/usr/bin/python3

# A simple script to apply a shader to all views except the active view
# When a new view is focused, the shader is applied to the previously
# active view. It skips app-id "panel", as this is wf-panel's app-id.

import os
import sys
from wayfire import WayfireSocket
from wayfire.extra.wpe import WPE

if len(sys.argv) == 1:
    print(f"Usage: {sys.argv[0]} /path/to/filters/shader")
    exit(-1)

sock = WayfireSocket()
wpe = WPE(sock)
sock.watch(['view-focused'])

def unset_view_shaders():
    for view in sock.list_views():
        wpe.filters_unset_view_shader(view["id"])

active_view_id = sock.get_focused_view()["id"]
active_view_app_id = sock.get_focused_view()["app-id"]
for view in sock.list_views():
    view_id = view["id"]
    if view_id != active_view_id and view["app-id"] != "panel":
        wpe.filters_set_view_shader(view_id, os.path.abspath(str(sys.argv[1])))
last_active_view_id = active_view_id
last_active_view_app_id = active_view_app_id

while True:
    try:
        msg = sock.read_next_event()
        if "event" in msg:
            active_view_id = sock.get_focused_view()["id"]
            active_view_app_id = sock.get_focused_view()["app-id"]
            if last_active_view_id != active_view_id and last_active_view_app_id != "panel":
                wpe.filters_set_view_shader(last_active_view_id, os.path.abspath(str(sys.argv[1])))
                wpe.filters_unset_view_shader(active_view_id)
            last_active_view_id = active_view_id
            last_active_view_app_id = active_view_app_id
    except KeyboardInterrupt:
        unset_view_shaders()
        exit(0)
    except:
        pass

