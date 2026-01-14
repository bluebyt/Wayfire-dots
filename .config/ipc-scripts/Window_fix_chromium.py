#!/usr/bin/env python3

from wayfire import WayfireSocket

APP_ID = "chromium"

TARGET_WIDTH = 1937
TARGET_HEIGHT = 1247

sock = WayfireSocket()
sock.watch(["view-mapped", "view-geometry-changed"])


def force_resize(view):
    # Ignore fullscreen or maximized windows
    if view.get("fullscreen") or view.get("maximized"):
        return

    geom = view.get("geometry")
    if not geom:
        return

    if geom["width"] == TARGET_WIDTH and geom["height"] == TARGET_HEIGHT:
        return

    print(
        f"Forcing {APP_ID} size: "
        f"{geom['width']}x{geom['height']} → {TARGET_WIDTH}x{TARGET_HEIGHT}"
    )

    sock.configure_view(
        view["id"],
        geom["x"],          # keep current position
        geom["y"],
        TARGET_WIDTH,
        TARGET_HEIGHT
    )


while True:
    event = sock.read_next_event()
    if not event or "event" not in event:
        continue

    if event["event"] not in ("view-mapped", "view-geometry-changed"):
        continue

    view = event.get("view")
    if not view:
        continue

    if view.get("app-id") != APP_ID:
        continue

    force_resize(view)
