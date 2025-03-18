zscroll -b "♪ x" -d 0.3 \
		-M "mpc status" \
		-m "playing" "-b ' '" \
		-m "paused" "-b ' ' -s 0" \
		-u t "mpc current"
