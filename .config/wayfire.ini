[alpha]
min_value = 0.100000
modifier = <alt> <super>

[animate]
close_animation = fire
duration = 300ms circle
enabled_for = (type equals "toplevel" | (type equals "x-or" & focusable equals true))
fade_duration = 400ms circle
fade_enabled_for = type equals "overlay"
fire_color = \#B22303FF
fire_duration = 300ms circle
fire_enabled_for = none
fire_particle_size = 16.000000
fire_particles = 2000
minimize_animation = zoom
open_animation = zoom
random_fire_color = false
spin_duration = 500ms linear
spin_rotations = 1
squeezimize_duration = 600ms linear
startup_duration = 600ms circle
zap_duration = 500ms linear
zoom_duration = 500ms circle
zoom_enabled_for = none

[annotate]
clear_workspace = <alt> <super> KEY_C
draw = <alt> <super> BTN_LEFT
from_center = true
line_width = 3.000000
method = draw
stroke_color = \#FF0000FF

[autorotate-iio]
lock_rotation = false
rotate_down = <ctrl> <super> KEY_DOWN
rotate_left = <ctrl> <super> KEY_LEFT
rotate_right = <ctrl> <super> KEY_RIGHT
rotate_up = <ctrl> <super> KEY_UP

[autostart]
0_0 = systemctl --user import-environment
autostart_wf_shell = false
background = wf-background
bar =
dock = wf-dock
gtk = sleep 1 && (XDG_SESSION_TYPE=wayland XDG_CURRENT_DESKTOP=sway)
portal = /usr/lib/xdg-desktop-portal --replace & /usr/lib/xdg-desktop-portal-wlr
launcher01 = /home/bluebyt/.bin/thunar.sh
launcher02 = kitty
launcher03 = wezterm
launcher04 = chromium --ozone-platform=wayland &
launcher05 = firefox
launcher06 = SDL_VIDEODRIVER=wayland lite-xl ~/.config/wayfire.ini ~/.Wayfirereadme.ini &
launcher07 = nautilus
launcher08 = blueman-manager
launcher09 = wcm
launcher10 = nwg-look
launcher11 = vesktop
launcher12 = ristretto -s /mnt/media/Deviant/Art6/evening_in_dystopia.jpg &
launcher13 = /home/bluebyt/.bin/mpv.sh
launcher14 = ~/.config/ipc-scripts/mpvrule1.py
launcher15 = ~/.config/ipc-scripts/mpvrule2.py
launcher16 = zeditor
launcher17 = ~/.config/scripts/./eww-start3.sh
launcher18 = ~/.config/ipc-scripts/workspace_update_style.py
launcher20 = ~/.config/scripts/zellij.sh
launcher21 = xfce4-terminal -e ncmpcpp
launcher22 = ulauncher --hide-window
launcher23 = swayosd-server
launcher24 = swayosd-libinput-backend
launcher25 = notify-send -a aurora "hello $(whoami)"
launcher26 = /usr/bin/xava
launcher27 = pactl load-module module-switch-on-connect
launcher28 = sleep 2 && swww-daemon && swww img ~/Pictures/Nord/Nord_wall2.jpeg
launcher29 = /home/bluebyt/.local/bin/ironbar
launcher30 = clapper /mnt/media/Videos/AI/MonacoRoyale-Sci-Fi.mp4
notifications = mako
polkit-gnome = /usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1

[background-view]
app_id =
command =
file =
inhibit_input = true

[bench]
average_frames = 25
position = top_center

[blur]
blur_by_default = type is "toplevel"
bokeh_degrade = 1
bokeh_iterations = 15
bokeh_offset = 5.000000
box_degrade = 1
box_iterations = 2
box_offset = 1.000000
gaussian_degrade = 1
gaussian_iterations = 2
gaussian_offset = 1.000000
kawase_degrade = 8
kawase_iterations = 2
kawase_offset = 2.000000
method = gaussian
saturation = 1.000000
toggle = none

[command]
binding_launcher = <ctrl> KEY_SPACE
binding_rofi = <ctrl> KEY_R
binding_logout = <super> KEY_ESC
binding_mute = KEY_MUTE
binding_screenshot = KEY_SYSRQ
binding_slurp = <ctrl> KEY_SYSRQ
binding_terminal = <super> KEY_ENTER
binding_voldown = KEY_VOLUMEDOWN
binding_volup = KEY_VOLUMEUP
command_launcher = ulauncher-toggle &
command_logout = wlogout
command_mute = swayosd-client --output-volume mute-toggle
command_screenshot = ~/.bin/grimshot.sh --notify save screen
command_slurp = grim -g "$(slurp)" - | swappy -f -
command_terminal = blackbox
command_voldown = wpctl set-volume @DEFAULT_AUDIO_SINK@ 5%- | swayosd-client --output-volume lower
command_volup = wpctl set-volume @DEFAULT_AUDIO_SINK@ 5%+ | swayosd-client --output-volume raise
command_rofi = rofi -show run


[core]
background_color = \#1A1A1AFF
close_top_view = <super> KEY_Q
exit = <alt> <ctrl> KEY_BACKSPACE
focus_button_with_modifiers = false
focus_buttons = BTN_LEFT | BTN_MIDDLE | BTN_RIGHT
focus_buttons_passthrough = true
max_render_time = -1
plugins = ipc ipc-rules stipc follow-focus alpha animate autostart command cube expo fast-switcher fisheye foreign-toplevel gtk-shell idle move place resize switcher vswitch window-rules wm-actions wobbly wrot scale wf-info pixdecor wsets wayfire-shell blur focus-change kbdd
preferred_decoration_mode = client
transaction_timeout = 100
vheight = 3
vwidth = 3
xwayland = true

[crosshair]
line_color = \#FF0000FF
line_width = 2

[cube]
activate = <alt> <ctrl> BTN_LEFT
background = \#1A1A1AFF
background_mode = simple
cubemap_image =
deform = 0
initial_animation = 350ms circle
light = true
rotate_left = none
rotate_right = none
skydome_mirror = true
skydome_texture =
speed_spin_horiz = 0.020000
speed_spin_vert = 0.020000
speed_zoom = 0.070000
zoom = 0.100000

[decoration]
active_color = \#222222AA
border_size = 0
button_order = minimize maximize close
font = sans-serif
ignore_views = none
inactive_color = \#333333DD
title_height = 0

[expo]
background = \#1A1A1AFF
duration = 300ms circle
inactive_brightness = 0.700000
keyboard_interaction = true
offset = 10
select_workspace_1 = <ctrl> KEY_1
select_workspace_2 = KEY_2
select_workspace_3 = KEY_3
select_workspace_4 = KEY_4
select_workspace_5 = KEY_5
select_workspace_6 = KEY_6
select_workspace_7 = KEY_7
select_workspace_8 = KEY_8
select_workspace_9 = KEY_9
toggle = <super>  | hotspot left-top 10x10 200
transition_length = 200

[extra-gestures]
close_fingers = 20
move_delay = 500
move_fingers = 3

[fast-switcher]
activate = <alt> KEY_ESC
activate_backward = <alt> <shift> KEY_ESC
inactive_alpha = 0.700000

[fisheye]
radius = 450.000000
toggle = <ctrl> <super> KEY_F
zoom = 7.000000

[focus-change]
cross-output = false
cross-workspace = false
down = <shift> <super> KEY_DOWN
grace-down = 15
grace-left = 13
grace-right = 13
grace-up = 11
left = <shift> <super> KEY_LEFT
raise-on-change = true
right = <shift> <super> KEY_RIGHT
scan-height = 9
scan-width = 12
up = <shift> <super> KEY_UP

[focus-steal-prevent]
cancel_keys = KEY_ENTER
deny_focus_views = none
timeout = 1000

[follow-focus]
change_output = true
change_view = true
focus_delay = 50
raise_on_top = true
threshold = 10

[force-fullscreen]
constrain_pointer = false
constraint_area = view
key_toggle_fullscreen = <alt> <super> KEY_F
preserve_aspect = true
transparent_behind_views = true
x_skew = 0.000000
y_skew = 0.000000

[foreign-toplevel]

[ghost]
ghost_match =
ghost_toggle =

[grid]
duration = 300ms circle
restore = <super> KEY_DOWN | <super> KEY_KP0
slot_b = <super> KEY_KP2
slot_bl = <super> KEY_KP1
slot_br = <super> KEY_KP3
slot_c = <super> KEY_UP | <super> KEY_KP5
slot_l = <super> KEY_LEFT | <super> KEY_KP4
slot_r = <super> KEY_RIGHT | <super> KEY_KP6
slot_t = <super> KEY_KP8
slot_tl = <super> KEY_KP7
slot_tr = <super> KEY_KP9
type = crossfade

[gtk-shell]

[hide-cursor]
hide_delay = 2000
toggle = <ctrl> <super> KEY_H

[hinge]
filename = /sys/bus/iio/devices/iio:device1/in_angl0_raw
flip_degree = 180
poll_freq = 200

[idle]
cube_max_zoom = 1.500000
cube_rotate_speed = 1.000000
cube_zoom_speed = 1000
disable_initially = false
disable_on_fullscreen = false
dpms_timeout = -1
screensaver_timeout = 120
toggle = none

[input]
click_method = default
cursor_size = 24
cursor_theme = Bibata-Modern-Classic
disable_touchpad_while_mouse = false
disable_touchpad_while_typing = false
drag_lock = false
gesture_sensitivity = 1.000000
kb_capslock_default_state = false
kb_numlock_default_state = true
kb_repeat_delay = 400
kb_repeat_rate = 40
left_handed_mode = false
middle_emulation = false
modifier_binding_timeout = 400
mouse_accel_profile = default
mouse_cursor_speed = 0.000000
mouse_natural_scroll = false
mouse_scroll_speed = 1.000000
natural_scroll = false
scroll_method = default
tablet_motion_mode = default
tap_to_click = true
touchpad_accel_profile = default
touchpad_cursor_speed = 0.000000
touchpad_scroll_speed = 1.000000
xkb_layout = us,ca
xkb_model = pc105
xkb_options = grp:alt_shift_toggle
xkb_rules = evdev
xkb_variant = altgr-intl

[input-device]
output =

[input-method-v1]
enable_text_input_v1 = true
enable_text_input_v3 = true

[invert]
preserve_hue = false
toggle = <super> KEY_I

[ipc]

[ipc-rules]

[join-views]

[kbdd]
export_layout_filename = /tmp/layout.json

[keycolor]
color = \#000000FF
opacity = 0.250000
threshold = 0.500000

[mag]
default_height = 500
toggle = <alt> <super> KEY_M
zoom_level = 75

[move]
activate = <super> BTN_LEFT
enable_snap = true
enable_snap_off = true
join_views = false
preview_base_border = \#404080CC
preview_base_color = \#8080FF80
preview_border_width = 3
quarter_snap_threshold = 50
snap_off_threshold = 200
snap_threshold = 10
workspace_switch_after = -1

[obs]

[oswitch]
next_output = <super> KEY_O
next_output_with_win = <shift> <super> KEY_O
prev_output =
prev_output_with_win =

[output]
depth = 8
mode = auto
position = auto
scale = 1.000000
transform = normal
vrr = false

[pin-view]

[pixdecor]
always_decorate = imv
animate = true
bg_color = \#1a1b26FF
bg_text_color = \#B3B3B3FF
border_size = 5
csd_titlebar_height = 32
effect_color = \#9D7CD8FF
effect_type = none
enable_shade = true
fg_color = \#1a1b26FF
fg_text_color = \#FFFFFFFF
ignore_views = (app_id is "ulauncher")
maximized_borders = true
maximized_shadows = true
overlay_engine = rounded_corners
rounded_corner_radius = 12
shade_duration = 1000ms sigmoid
shade_modifier = <ctrl> <super>
shade_toggle =
shadow_color = \#00000040
shadow_radius = 10
title_text_align = 1
titlebar = false

[place]
mode = center

[preserve-output]
last_output_focus_timeout = 10000

[resize]
activate = <super> BTN_RIGHT
activate_preserve_aspect = none

[scale]
allow_zoom = false
bg_color = \#1A1A1AE6
close_on_new_view = false
duration = 400ms circle
inactive_alpha = 0.750000
include_minimized = false
interact = false
middle_click_close = false
minimized_alpha = 0.450000
outer_margin = 0
spacing = 50
text_color = \#CCCCCCFF
title_font_size = 16
title_overlay = all
title_position = center
toggle = <super> KEY_P
toggle_all = <super> KEY_W

[scale-title-filter]
bg_color = \#00000080
case_sensitive = false
font_size = 30
overlay = true
share_filter = false
text_color = \#CCCCCCCC

[session-lock]

[shortcuts-inhibit]
break_grab = none
ignore_views = none
inhibit_by_default = none

[showrepaint]
reduce_flicker = true
toggle = <alt> <super> KEY_S

[simple-tile]
animation_duration = 0ms circle
button_move = <super> BTN_LEFT
button_resize = <super> BTN_RIGHT
inner_gap_size = 2
keep_fullscreen_on_adjacent = true
key_focus_above = <super> KEY_K
key_focus_below = <super> KEY_J
key_focus_left = <super> KEY_H
key_focus_right = <super> KEY_L
key_toggle = <super> KEY_T
outer_horiz_gap_size = 0
outer_vert_gap_size = 0
preview_base_border = \#404080CC
preview_base_color = \#8080FF80
preview_border_width = 3
tile_by_default = all

[switcher]
next_view = <alt> KEY_TAB
prev_view = <alt> <shift> KEY_TAB
speed = 500ms circle
view_thumbnail_rotation = 30
view_thumbnail_scale = 1.000000

[view-shot]
capture = <alt> <super> BTN_MIDDLE
command = notify-send "The view under cursor was captured to %f"
filename = /tmp/snapshot-%F-%T.png

[vswipe]
background = \#1A1A1AFF
delta_threshold = 24.000000
duration = 180ms circle
enable_free_movement = false
enable_horizontal = true
enable_smooth_transition = false
enable_vertical = true
fingers = 4
gap = 32.000000
speed_cap = 0.050000
speed_factor = 256.000000
threshold = 0.350000

[vswitch]
background = \#1A1A1AFF
binding_down = <ctrl> KEY_DOWN
binding_last =
binding_left = <ctrl> KEY_LEFT
binding_right = <ctrl> KEY_RIGHT
binding_up = <ctrl> KEY_UP
duration = 300ms circle
gap = 20
send_win_down =
send_win_last =
send_win_left =
send_win_right =
send_win_up =
with_win_down = <ctrl> <super> KEY_DOWN
with_win_last =
with_win_left = <ctrl> <super> KEY_LEFT
with_win_right = <ctrl> <super> KEY_RIGHT
with_win_up = <ctrl> <super> KEY_UP
wraparound = true

[water]
activate = <ctrl> <super> BTN_LEFT

[wayfire-shell]
toggle_menu = <super>

[wf-info]

[window-rules]
rule_001 = on created if app_id is "thunar" then set geometry 236 83 886 552
rule_002 = on created if app_id is "thunar" then set alpha 0.8
rule_003 = on created if title contains "Rename" then set geometry 485 241 418 215
rule_004 = on created if title contains "Properties" then set geometry 378 91 572 541
rule_005 = on created if title is "bluebyt - Thunar" then assign_workspace 0 0
rule_006 = on created if title is "Downloads - Thunar" then assign_workspace 2 0
rule_007 = on created if title is "media - Thunar" then assign_workspace 2 2
rule_008 = on created if app_id is "Alacritty" then set geometry 285 55 1767 1229
rule_009 = on created if app_id is "Alacritty" then assign_workspace 0 2
rule_010 = on created if app_id is "Alacritty" then set alpha 0.8
rule_011 = on created if app_id is "kitty" then move 239 664
rule_012 = on created if app_id is "kitty" then set alpha 0.8
rule_013 = on created if app_id is "kitty" then assign_workspace 0 0
rule_014 = on created if app_id is "brave-browser-beta" then set geometry 241 58 1865 1217
rule_015 = on created if app_id is "brave-browser-beta" then set alpha 1.0
rule_016 = on created if app_id is "brave-browser-beta" then assign_workspace 1 0
rule_017 = on created if app_id is "org.wezfurlong.wezterm" then set geometry 279 647 833 518
rule_018 = on created if app_id is "org.wezfurlong.wezterm" then set alpha 0.8
rule_019 = on created if app_id is "org.wezfurlong.wezterm" then assign_workspace 2 0
rule_020 = on created if app_id is "lite-xl" then set geometry 1121 53 1095 1214
rule_021 = on created if app_id is "lite-xl" then set alpha 0.9
rule_022 = on created if app_id is "lite-xl" then assign_workspace 2 0
rule_023 = on created if app_id is "org.gnome.TextEditor" then move 1160 80
rule_024 = on created if app_id is "org.gnome.TextEditor" then set alpha 0.8
rule_025 = on created if app_id is "org.gnome.TextEditor" then assign_workspace 2 0
rule_026 = on created if app_id is "nwg-look" then set geometry 238 136 965 519
rule_027 = on created if app_id is "nwg-look" then set alpha 0.8
rule_028 = on created if app_id is "nwg-look" then assign_workspace 0 1
rule_029 = on created if app_id is "blueman-manager" then set geometry 363 796 640 500
rule_030 = on created if app_id is "blueman-manager" then set alpha 0.7
rule_031 = on created if app_id is "blueman-manager" then assign_workspace 0 1
rule_032 = on created if app_id is "org.pulseaudio.pavucontrol" then set geometry 280 710 800 500
rule_033 = on created if app_id is "org.pulseaudio.pavucontrol" then set alpha 0.9
rule_034 = on created if app_id is "org.pulseaudio.pavucontrol" then assign_workspace 0 1
rule_035 = on created if app_id is "firefox" then set geometry 266 43 1846 1203
rule_036 = on created if app_id is "firefox" then set alpha 1.0
rule_037 = on created if app_id is "firefox" then assign_workspace 1 1
rule_038 = on created if title contains "Save Image" then set geometry 485 241 418 215
rule_039 = on created if app_id is "chromium" then set geometry 259 39 1932 1226
rule_040 = on created if app_id is "chromium" then set alpha 1.0
rule_041 = on created if app_id is "chromium" then assign_workspace 1 0
rule_042 = on created if app_id is "ristretto" then assign_workspace 2 1
rule_043 = on created if app_id is "ristretto" then set alpha 0.8
rule_044 = on created if app_id is "foot" then move 263 672
rule_045 = on created if app_id is "foot" then set alpha 0.8
rule_046 = on created if app_id is "vesktop" then set geometry 412 62 1774 1251
rule_047 = on created if app_id is "vesktop" then set alpha 0.8
rule_048 = on created if app_id is "vesktop" then assign_workspace 1 2
rule_049 = on created if app_id is "xfce4-terminal" then set geometry 462 234 833 532
rule_050 = on created if app_id is "xfce4-terminal" then set alpha 0.8
rule_051 = on created if app_id is "xfce4-terminal" then assign_workspace 0 0
rule_052 = on created if app_id is "pcmanfm" then move 270 100
rule_053 = on created if app_id is "pcmanfm" then assign_workspace 2 2
rule_054 = on created if app_id is "ulauncher" then center
rule_055 = on created if app_id is "ulauncher" then set alpha 0.7
rule_056 = on created if app_id is "Conky" then set sticky
rule_057 = on created if app_id is "com.github.rafostar.Clapper" then set geometry 1350 720 750 500
rule_058 = on created if app_id is "com.github.rafostar.Clapper" then assign_workspace 2 2
rule_059 = on created if app_id is "GStreamer gst-play-1.0" then set geometry 1350 820 750 500
rule_060 = on created if app_id is "nemo org.Nemo" then set alpha 0.8
rule_061 = on created if app_id is "nemo org.Nemo" then assign_workspace 1 2
rule_062 = on created if title contains "Manipulation Program" then move 270 70
rule_063 = on created if title contains "Manipulation Program" then set alpha 0.9
rule_064 = on created if title contains "Manipulation Program" then assign_workspace 2 2

rule_065 = on created if app_id is "org.gnome.Ptyxis.Devel" then set geometry 278 689 812 494
rule_066 = on created if app_id is "org.gnome.Ptyxis.Devel" then set alpha 0.8
rule_067 = on created if app_id is "org.gnome.Ptyxis.Devel" then assign_workspace 2 0
rule_068 = on created if app_id is "com.raggesilver.BlackBox" then move 270 700
rule_0661 = on created if app_id is "com.raggesilver.BlackBox" then set alpha 0.8
rule_069 = on created if app_id is "com.raggesilver.BlackBox" then assign_workspace 2 2
rule_070 = on created if app_id is "io.github.celluloid_player.Celluloid" then set geometry 1754 191 720 503
rule_071 = on created if app_id is "org.kde.kdenlive" then set alpha 0.9
rule_072 = on created if app_id is "org.kde.kdenlive" then assign_workspace 2 2
rule_073 = on created if app_id is "panel" then set alpha 0.6
rule_074 = on created if title contains "Rendering — Kdenlive" then set geometry 424 286 938 591
rule_075 = on created if title is "Picture-in-Picture" then set always_on_top
rule_076 = on created if app_id is "wcm" then set geometry 1195 140 1044 624
rule_077 = on created if app_id is "wcm" then set alpha 0.8
rule_078 = on created if app_id is "wcm" then assign_workspace 0 1
rule_079 = on created if app_id is "mpv" then set geometry 1304 717 812 476
rule_080 = on created if app_id is "mpv" then assign_workspace 0 0
rule_081 = on created if title is "Anton_Ishutin.mp4 - mpv" then assign_workspace 0 0
rule_082 = on created if title is "Paramore Last Hope.mp4 - mpv" then assign_workspace 2 2
rule_083 = on created if app_id is "pcmanfm" then set alpha 0.8
rule_084 = on created if app_id is "org.gnome.Nautilus" then set geometry 263 232 797 611
rule_085 = on created if app_id is "org.gnome.Nautilus" then set alpha 0.9
rule_086 = on created if app_id is "org.gnome.Nautilus" then assign_workspace 0 2
# rule_087 = on created if app_id is "notifications" then set alpha 0.7
rule_088 = on created if app_id is "org.gnome.NautilusPreviewer" then move 270 70
rule_089 = on created if app_id is "geany" then set alpha 0.8
rule_090 = on created if app_id is "dev.zed.Zed" then set geometry 1088 228 1086 1010
rule_091 = on created if app_id is "dev.zed.Zed" then set alpha 0.8
rule_092 = on created if app_id is "dev.zed.Zed" then assign_workspace 0 2
rule_093 = on created if app_id is "rio" then set alpha 0.8
rule_094 = on created if app_id contains "keepass" then set alpha 0.8
rule_095 = on created if app_id contains "xfce4-taskmanager" then set alpha 0.8
rule_096 = on created if app_id contains "rofi" then set alpha 0.8
rule_097 = on created if app_id contains "ironbar" then set alpha 0.9
rule_098 = on created if app_id contains "tilix" then set alpha 0.7
rule_099 = on created if app_id contains "org.gnome.World.Secrets" then set alpha 0.7
rule_100 = on created if app_id contains "org.gnome.Terminal" then set alpha 0.7
rule_101 = on created if app_id is "org.gnome.Epiphany" then set geometry 389 66 1811 1188
rule_102 = on created if app_id is "org.gnome.Epiphany" then set alpha 0.9
rule_103 = on created if app_id is "org.gnome.Epiphany" then assign_workspace 1 2
rule_104 = on created if app_id is "so.libdb.dissent" then set geometry 317 73 1650 1144
rule_105 = on created if app_id is "so.libdb.dissent" then set alpha 0.9
rule_106 = on created if app_id is "so.libdb.dissent" then assign_workspace 1 2
rule_107 = on created if app_id is "net.nokyan.Resources" then set geometry 1163 70 926 567
rule_108 = on created if app_id is "net.nokyan.Resources" then set alpha 0.8
rule_109 = on created if app_id is "net.nokyan.Resources" then assign_workspace 0 2
rule_107 = on created if app_id is "org.gnome.Showtime" then set geometry 1361 740 829 469
rule_108 = on created if app_id is "org.gnome.Showtime" then set alpha 1.0
rule_109 = on created if app_id is "org.gnome.Showtime" then assign_workspace 2 2

[winzoom]
dec_x_binding = <ctrl> <super> KEY_LEFT
dec_y_binding = <ctrl> <super> KEY_UP
inc_x_binding = <ctrl> <super> KEY_RIGHT
inc_y_binding = <ctrl> <super> KEY_DOWN
modifier = <ctrl> <super>
nearest_filtering = false
preserve_aspect = true
zoom_step = 0.100000

[wm-actions]
minimize = none
send_to_back = none
toggle_always_on_top = none
toggle_fullscreen = none
toggle_maximize = none
toggle_showdesktop = none
toggle_sticky = none

[wobbly]
friction = 3.000000
grid_resolution = 6
spring_k = 8.000000

[workarounds]
all_dialogs_modal = true
app_id_mode = full
discard_command_output = true
dynamic_repaint_delay = false
enable_input_method_v2 = false
enable_opaque_region_damage_optimizations = false
enable_so_unloading = false
force_preferred_decoration_mode = false
remove_output_limits = false
use_external_output_configuration = false

[workspace-names]
background_color = \#333333B3
background_radius = 30.000000
display_duration = 500
font = sans-serif
margin = 0
position = center
show_option_names = false
text_color = \#FFFFFFFF

[wrot]
activate = <ctrl> <super> BTN_RIGHT
activate-3d = <shift> <super> BTN_RIGHT
invert = false
reset = <ctrl> <super> KEY_R
reset-one = <super> KEY_R
reset_radius = 25.000000
sensitivity = 24

[wsets]
label_duration = 2000ms circle

[xdg-activation]

[zoom]
interpolation_method = 0
modifier = <super>
smoothing_duration = 300ms circle
speed = 0.010000
