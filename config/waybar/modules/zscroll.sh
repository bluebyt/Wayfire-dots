#!/usr/bin/env bash

zscroll --before-text " x" --delay 0.3 \
    --length 20 \
		--match-command "mpc status" \
		--match-text "playing" "--before-text ' ' --scroll 1" \
		--match-text "paused" "--before-text ' ' --scroll 0" \
		--update-interval 1 \
		--update-check true "mpc current" &

wait
