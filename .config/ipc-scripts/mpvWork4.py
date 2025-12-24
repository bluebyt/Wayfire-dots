#!/usr/bin/python3

from wayfire import WayfireSocket

sock = WayfireSocket()
sock.watch(['view-mapped'])

while True:
    msg = sock.read_next_event()
    
    # The view-mapped event is emitted when a new window has been opened.
    if "event" in msg:
        view = msg["view"]

        # Check for "Paramore Last Hope.mp4 - mpv"
        if view["title"] == "Paramore Last Hope.mp4 - mpv":
            sock.configure_view(view["id"], 1304, 717, 812, 476)
            sock.set_workspace(2, 2, view["id"]) 

        # Check for "Faraon - Alone Tonight.mp4"
        elif view["title"] == "Faraon - Alone Tonight.mp4":
            sock.configure_view(view["id"], 1304, 717, 812, 476)
            sock.set_workspace(0, 0, view["id"])
