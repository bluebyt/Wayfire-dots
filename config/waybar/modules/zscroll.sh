#!/usr/bin/env bash

zscroll --before-text " x" --delay 0.3 \
		--match-command "mpc status" \
		--match-text "playing" "--before-text ' '" \
		--match-text "paused" "--before-text ' ' --scroll 0" \
		--update-check true "mpc current" &

wait

