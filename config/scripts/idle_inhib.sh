#!/bin/sh

IDLE_STATUS=`ps ax | grep swayidle | grep -v grep | grep "2700"  | sed "s/^\s*//" | cut -d " " -f 1`

if [[ -n "$IDLE_STATUS" ]]; then
	# idle inhibitor is not normal
	# /usr/bin/wayland-idle-inhibitor.py &
	killall swayidle
	swayidle -w timeout 43200 "$HOME/.config/scripts/lock.sh" timeout 48200 'hyprctl dispatch dpms off' resume 'hyprctl dispatch dpms on' &
	eww update idle_state="" &
	notify-send -e "swayidle is extended" &
else
	#idle inhibitor is running, kill it
	killall swayidle
	swayidle -w timeout 2700 "$HOME/.config/scripts/lock.sh" timeout 7200 'hyprctl dispatch dpms off' resume 'hyprctl dispatch dpms on' &
	eww update idle_state="" &
	notify-send -e "swayidle is normal" &
fi
