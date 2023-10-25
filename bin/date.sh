#!/bin/bash

icon="/home/bluebyt/.icons/dracula-icons-main/scalable/apps/date.svg"
title="$(date +%H:%M)"
text="$(date +%d). $(date +%B) $(date +%Y), $(date +%A)"

notify-send -i $icon "$title" "$text"
