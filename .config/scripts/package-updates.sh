#!/bin/sh
format() {
	if [ "$1" -eq 0 ]; then
		echo '-'
	else
		echo "$1"
	fi
}

updates_arch=$(checkupdates 2>/dev/null | wc -l)
updates_aur=$(paru -Qum 2>/dev/null | wc -l)
updates=$((updates_arch + updates_aur))

if [ "$updates" -gt 0 ]; then
	echo "$(format "$updates_arch")/$(format "$updates_aur")"
else
	echo "Up to date"
fi

