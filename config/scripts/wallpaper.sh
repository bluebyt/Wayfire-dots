#!/bin/sh

folder="${HOME}/Pictures"
pic=$(ls $folder/* | shuf -n1)

# hyprctl hyprpaper wallpaper eDP-1,"file://$pic"

swww img -t any --transition-fps 90 $pic & &>/dev/null
sleep 1
