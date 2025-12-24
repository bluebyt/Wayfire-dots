#!/usr/bin/env python3

from wayfire.ipc import WayfireSocket

def print_current_layout_code():
    sock = WayfireSocket()
    keyboard = sock.get_keyboard_layout()

    layouts = keyboard.get("possible-layouts", [])
    index = keyboard.get("layout-index", 0)

    # Map full names to short codes
    layout_map = {
        "English (intl., with AltGr dead keys)": "us",
        "English (US)": "us",
        "French (Canada)": "ca",
        "French": "fr",
    }

    if layouts and 0 <= index < len(layouts):
        full = layouts[index]
        print(layout_map.get(full, "??"))
    else:
        print("??")

if __name__ == "__main__":
    print_current_layout_code()

