#!/usr/bin/env python3
import time
from wayfire import WayfireSocket


RULES = [
    {"app_id": "thunar", "geometry": (236, 83, 886, 552), "alpha": 0.8},
    {"title": "Rename", "geometry": (485, 241, 418, 215)},
    {"title": "Properties", "geometry": (378, 91, 572, 541)},
    {"app_id": "Alacritty", "geometry": (797, 277, 933, 636), "alpha": 0.8},
    {"title": "kittyfirst", "geometry": (259, 662, 786, 480), "alpha": 0.8, "workspace": (0, 0)},
    {"title": "kittymain", "geometry": (248, 648, 788, 566), "alpha": 0.8, "workspace": (2, 0)},
    {"title": "kittylayout", "geometry": (247, 51, 1920, 1203), "alpha": 0.8, "workspace": (0, 2)},
    {"app_id": "brave-browser", "geometry": (236, 51, 1990, 1232), "alpha": 1.0, "workspace": (1, 0)},
    {"app_id": "org.wezfurlong.wezterm", "geometry": (253, 667, 969, 627), "alpha": 0.8, "workspace": (2, 2)},
    {"app_id": "com.lite_xl.LiteXL", "geometry": (1027, 43, 1213, 1223), "alpha": 0.8, "workspace": (2, 0)},
    {"app_id": "org.gnome.TextEditor", "geometry": (1057, 55, 1164, 1201), "alpha": 0.8, "workspace": (2, 0)},
    {"app_id": "nwg-look", "geometry": (261, 95, 965, 519), "alpha": 0.8, "workspace": (0, 1)},
    {"app_id": "blueman-manager", "geometry": (363, 796, 640, 500), "alpha": 0.7, "workspace": (0, 1)},
    {"app_id": "org.pulseaudio.pavucontrol", "geometry": (282, 86, 800, 500), "alpha": 0.9, "workspace": (0, 1)},
    {"app_id": "firefox", "geometry": (273, 70, 1900, 1174), "alpha": 1.0, "workspace": (1, 1)},
    {"app_id": "chromium", "geometry": (250, 51, 1946, 1252), "alpha": 1.0, "workspace": (1, 0)},
    {"app_id": "org.xfce.ristretto","geometry": (517, 116, 1531, 1040), "alpha": 0.8, "workspace": (2, 1)},
    {"app_id": "foot", "move": (263, 672), "alpha": 0.8},
    {"app_id": "vesktop", "geometry": (412, 62, 1774, 1251), "alpha": 0.8, "workspace": (1, 2)},
    {"app_id": "xfce4-terminal", "geometry": (1350, 87, 728, 475), "alpha": 0.8, "workspace": (0, 0)},
    {"app_id": "pcmanfm", "move": (270, 100), "alpha": 0.8, "workspace": (2, 2)},
    {"app_id": "ulauncher", "alpha": 0.8},
    {"app_id": "Conky", "sticky": True},
    {"title": "BountyHunterGalacticAdventures", "geometry": (1423, 679, 685, 442), "workspace": (2, 2)},
    {"title": "FutureBeauty", "geometry": (1350, 720, 750, 500), "workspace": (0, 0)},
    {"title": "Manipulation Program", "move": (270, 70), "alpha": 0.9, "workspace": (2, 2)},
    {"app_id": "org.gnome.Ptyxis", "geometry": (251, 663, 726, 492), "alpha": 0.8, "workspace": (2, 0)},
    {"app_id": "com.raggesilver.BlackBox", "geometry": (298, 674, 1008, 624), "alpha": 0.8, "workspace": (2, 2)},
    {"app_id": "io.github.celluloid_player.Celluloid", "geometry": (1489, 356, 726, 510)},
    {"app_id": "org.kde.kdenlive", "alpha": 0.9, "workspace": (2, 2)},
    {"app_id": "panel", "alpha": 0.6},
    {"title": "Rendering — Kdenlive", "geometry": (865, 398, 960, 800)},
    {"title": "Picture-in-Picture", "always_on_top": True},
    {"app_id": "wcm", "geometry": (1280, 691, 977, 550), "alpha": 0.8, "workspace": (0, 1)},
    {"app_id": "org.gnome.Nautilus", "alpha": 0.9},
    {"app_id": "org.gnome.NautilusPreviewer", "geometry": (1012, 211, 632, 1173)},
    {"app_id": "geany", "alpha": 0.8},
    {"app_id": "dev.zed.Zed", "geometry": (1083, 67, 1110, 1147), "alpha": 0.8, "workspace": (2, 0)},
    {"app_id_contains": "keepass", "alpha": 0.8},
    {"app_id_contains": "xfce4-taskmanager", "alpha": 0.8},
    {"app_id_contains": "rofi", "alpha": 0.9},
    {"app_id_contains": "ironbar", "alpha": 0.9},
    {"app_id": "org.gnome.World.Secrets", "geometry": (269, 652, 851, 531), "alpha": 0.7, "workspace": (0, 1)},
    {"app_id": "org.gnome.Epiphany", "geometry": (389, 66, 1811, 1188), "alpha": 1.0, "workspace": (1, 2)},
    {"app_id": "so.libdb.dissent", "geometry": (317, 73, 1650, 1144), "alpha": 0.9, "workspace": (1, 2)},
    {"title": "Resources", "geometry": (1304, 87, 859, 570), "alpha": 0.8, "workspace": (0, 1)},
    {"app_id": "org.gnome.Showtime", "geometry": (1558, 336, 468, 832), "workspace": (2, 2)},
    {"app_id": "xdg-desktop-portal-gtk", "geometry": (805, 303, 892, 527), "alpha": 0.8},
    {"app_id": "rio", "geometry": (1331, 80, 850, 550), "alpha": 0.8, "workspace": (0, 0)},
    {"app_id": "org.gnome.SystemMonitor", "geometry": (1293, 105, 818, 549), "alpha": 0.8, "workspace": (0, 1)},
    {"app_id": "feh", "move": (1125, 135)},
    {"app_id": "com.github.neithern.g4music", "geometry": (1479, 86, 705, 512), "alpha": 0.8, "workspace": (0, 2)},
    {"app_id": "io.github.amit9838.mousam", "alpha": 0.8},
    {"title": "File Upload", "geometry": (776, 323, 873, 489), "alpha": 0.8},
    {"app_id": "org.gnome.Loupe", "geometry": (1402, 675, 685, 480)},
    {"app_id": "gtk-layer-shell", "alpha": 0.9},
    {"app_id": "com.github.wwmm.easyeffects", "alpha": 0.8},
    {"app_id": "org.gnome.Calculator", "alpha": 0.7},
    {"app_id": "spotube", "alpha": 0.7},
    {"title": "Better Control", "geometry": (295, 634, 900, 636), "alpha": 0.7, "workspace": (0, 1)},
    {"app_id": "de.haeckerfelix.Fragments", "alpha": 0.7},
    {"app_id": "viewnior", "geometry": (1407, 472, 824, 710), "alpha": 0.8},
    {"app_id": "org.gnome.Totem", "geometry": (1363, 658, 763, 492), "alpha": 1.0, "workspace": (0, 0)},
    {"app_id": "org.nickvision.tubeconverter", "geometry": (1423, 98, 692, 621), "alpha": 0.8, "workspace": (2, 2)},
    {"app_id": "com.mitchellh.ghostty", "geometry": (298, 695, 705, 508), "alpha": 0.8, "workspace": (2, 0)},
    {"app_id": "waypaper", "geometry": (1273, 686, 843, 636), "alpha": 0.8, "workspace": (0, 1)},
    {"app_id": "clipse", "alpha": 0.8},
    {"app_id": "org.gnome.Terminal", "geometry": (289, 82, 1861, 1188), "alpha": 0.8, "workspace": (0, 2)},
    {"app_id": "com.toolstack.Folio", "alpha": 0.8},
    {"app_id": "io.missioncenter.MissionCenter", "alpha": 0.8},
    {"app_id": "tilix", "geometry": (1364, 102, 775, 478), "alpha": 0.8, "workspace": (0, 0)},
    {"app_id": "quickshell", "alpha": 0.8},
    {"app_id": "io.github.TheWisker.Cavasik", "alpha": 0.8},
    {"app_id": "zen", "geometry": (255, 72, 1971, 1189), "alpha": 1.0, "workspace": (1, 1)},
    {"app_id": "org.gnome.gedit", "geometry": (1130, 62, 1071, 1150), "alpha": 0.8, "workspace": (2, 0)},
    {"app_id": "com.github.rafostar.Clapper", "geometry": (1358, 450, 739, 415)},
    {"title": "Save Image", "geometry": (659, 355, 890, 611)},
    {"app_id": "fsearch", "geometry": (296, 82, 888, 513), "alpha": 0.8, "workspace": (0, 1)},
    {"app_id": "btm-toggle", "geometry": (1862, 26, 710, 1203), "alpha": 0.7},
    {"title": "SleepToken", "geometry": (1570, 450, 427, 757), "workspace": (2, 2)},
    {"title": "BountyHunterGalactic", "geometry": (1389, 734, 739, 415), "workspace": (0, 0)},
    {"app_id": "org.gnome.Meld", "alpha": 0.7},
    {"app_id": "im.riot.Riot", "geometry": (348, 62, 1823, 1254), "alpha": 0.8, "workspace": (1, 2)},
    {"title": "Open Files", "geometry": (877, 394, 920, 508)},
    {"title": "Open Image", "geometry": (877, 394, 920, 508)},
    {"app_id": "gimp", "move": (245, 61), "alpha": 1.0, "workspace": (2, 2)},
    {"app_id": "com.example.Nordic", "alpha": 0.8},
    {"app_id": "helium", "geometry": (250, 51, 1946, 1252), "alpha": 1.0, "workspace": (1, 0)},
    {"app_id": "mpv", "geometry": (1329, 671, 818, 482), "workspace": (0, 0)},
    {"app_id": "org.inkscape.Inkscape", "geometry": (291, 84, 1784, 1058), "workspace": (0, 2)},
    {"app_id": "vivaldi-stable", "geometry": (250, 51, 1946, 1252), "alpha": 1.0, "workspace": (1, 0)},
    {"title": "Save", "geometry": (781, 249, 770, 462)},
    {"title": "Save As", "geometry": (781, 249, 770, 462)},
    {"title": "file to save", "geometry": (722, 288, 934, 567)},
]

def matches_rule(view, rule):
    app_id = view.get("app-id", "")
    title = view.get("title", "")

    if "app_id" in rule and rule["app_id"] == app_id:
        return True
    if "app_id_contains" in rule and rule["app_id_contains"] in app_id:
        return True
    if "title" in rule and rule["title"] in title:
        return True
    return False

def apply_rule(sock, view_id, rule):
    if "geometry" in rule:
        x, y, w, h = rule["geometry"]
        sock.configure_view(view_id, x, y, w, h)
    elif "move" in rule:
        x, y = rule["move"]
        # Retain width/height while moving x, y
        view_info = sock.get_view(view_id)
        if view_info and "geometry" in view_info:
            w = view_info["geometry"]["width"]
            h = view_info["geometry"]["height"]
            sock.configure_view(view_id, x, y, w, h)

    if "alpha" in rule:
        sock.set_view_alpha(view_id, rule["alpha"])
        
    if "workspace" in rule:
        ws_x, ws_y = rule["workspace"]
        sock.send_view_to_workspace(view_id, ws_x, ws_y)

    if rule.get("sticky"):
        sock.set_view_sticky(view_id, True)

    if rule.get("always_on_top"):
        sock.set_view_always_on_top(view_id, True)

def main():
    sock = WayfireSocket()
    sock.watch()

    while True:
        try:
            msg = sock.read_next_event()
            if not msg:
                continue

            # Process view lifecycle events
            if msg.get("event") in ["view-mapped", "view-created", "view-title-changed"]:
                view = msg.get("view", {})
                view_id = view.get("id")

                if not view_id:
                    continue

                for rule in RULES:
                    if matches_rule(view, rule):
                        apply_rule(sock, view_id, rule)

        except Exception as e:
            time.sleep(0.1)

if __name__ == "__main__":
    main()
