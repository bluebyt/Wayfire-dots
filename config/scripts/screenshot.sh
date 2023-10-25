#!/bin/sh

sleep 1
#grimblast --notify save area ~/Pictures/Screenshots/$(date +'%s_screenshot.png') &>/dev/null
slurp | grim -g - ~/Downloads/slurped.png
