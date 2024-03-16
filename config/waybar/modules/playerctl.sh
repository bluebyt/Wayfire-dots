#!/usr/bin/env bash
exec 2> "$XDG_RUNTIME_DIR/waybar-playerctl.log"
IFS=$'\n\t'

while true; do

	while read -r playing position length line; do
		# json escaping
		line="${line//\"/\\\"}"
		((percentage = length ? (100 * (position % length)) / length : 0))
		case $playing in
			Paused) text='<span foreground=\"#cccc00\" size=\"smaller\">'"$line"'</span>' ;;
			Playing) text="<small>$line</small>" ;;
			*)text='<span foreground=\"#073642\">⏹</span>' ;;
		esac

		# exit if print fails
		printf '{"text":"%s","tooltip":"%s","class":"%s","percentage":%s}\n' \
			"$text" "$playing" "$percentage" "$percentage" || break 2

	done < <(
		# requires playerctl>=2.0
		playerctl --follow metadata --player strawberry,clementine,spotify,%any --format \
			$'{{status}}\t{{position}}\t{{mpris:length}}\t{{markup_escape(artist)}} - {{markup_escape(title)}} {{duration(position)}}|{{duration(mpris:length)}}' &
		echo $! > "$XDG_RUNTIME_DIR/waybar-playerctl.pid"
	)

	# no current players
	# exit if print fails
	echo '<span foreground=#dc322f>⏹</span>' || break
	sleep 15

done

kill "$(< "$XDG_RUNTIME_DIR/waybar-playerctl.pid")"
