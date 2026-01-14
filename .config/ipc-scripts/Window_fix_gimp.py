#!/usr/bin/env python3

from wayfire import WayfireSocket

APP_ID = "gimp"

TARGET_WIDTH = 1990
TARGET_HEIGHT = 1232

# Dialog title keywords to ignore (case-insensitive)
IGNORE_TITLE_KEYWORDS = (
    "save",
    "Save",
    "Save Image",
    "Save As",
    "open",
    "find",
)

sock = WayfireSocket()
sock.watch(["view-mapped", "view-geometry-changed"])


def force_resize(view):
    # Ignore fullscreen or maximized windows
    if view.get("fullscreen") or view.get("maximized"):
        return

    # Ignore dialog windows by title (case-insensitive match)
    title = view.get("title", "").lower()
    if any(keyword in title for keyword in IGNORE_TITLE_KEYWORDS):
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
        geom["x"],
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
