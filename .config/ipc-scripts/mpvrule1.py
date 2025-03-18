#!/usr/bin/python3

from wayfire import WayfireSocket

sock = WayfireSocket()
sock.watch(['view-mapped'])

while True:
    msg = sock.read_next_event()
    # The view-mapped event is emitted when a new window has been opened.
    if "event" in msg:
        view = msg["view"]
        if view["title"] == "mpvChillout.mp4 - mpv":
            sock.configure_view(view["id"], 1304, 717, 812, 476)
            sock.set_workspace(0, 0, view["id"])
 #          exit(0)
