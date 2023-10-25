#!/usr/bin/env bash
n=$(checkupdates | wc -l)
if [ "$n" != "0" ]; then
    notify-send "System update" "$n updates available."
fi
