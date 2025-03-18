#!/usr/bin/python3

from wayfire import WayfireSocket
from wayfire.extra.stipc import Stipc

class WayfireUtils:
    def __init__(self, socket: WayfireSocket):
        self._socket = socket

    def get_focused_view_title(self):
        """
        Retrieve the title of the currently focused view.

        Returns:
            str: The cropped title of the focused view, or None if no view is focused.
        """
        focused_view = self._socket.get_focused_view()
        title = focused_view.get("title") if focused_view else None
        if title:
            return title[:20] + "..." if len(title) > 20 else title
        return None

# Main script
if __name__ == "__main__":
    # Initialize Wayfire socket and utils
    socket = WayfireSocket()
    utils = WayfireUtils(socket)

    # Get and display the cropped focused window title
    focused_title = utils.get_focused_view_title()
    if focused_title:
        print(focused_title)
    else:
        print("No focused window.")

