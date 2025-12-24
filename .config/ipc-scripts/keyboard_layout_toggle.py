#!/usr/bin/env python3

from wayfire.ipc import WayfireSocket

def toggle_layout():
    sock = WayfireSocket()
    keyboard = sock.get_keyboard_layout()

    layouts = keyboard.get("possible-layouts", [])
    index = keyboard.get("layout-index", 0)

    if not layouts:
        print("No layouts configured.")
        return

    # Cycle to the next layout
    next_index = (index + 1) % len(layouts)
    sock.set_keyboard_layout(next_index)
    print(f"Toggled to: {layouts[next_index]}")

if __name__ == "__main__":
    toggle_layout()

