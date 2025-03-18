#!/bin/bash

# Store the current volume level
current_volume=$(pactl list sinks | grep 'Volume: front-left' | awk '{print $5}' | cut -d '%' -f1 | tr -d '\n')

while true; do
    # Check for volume changes
    new_volume=$(pactl list sinks | grep 'Volume: front-left' | awk '{print $5}' | cut -d '%' -f1 | tr -d '\n')

    # If the volume has changed, play a sound
    if [ "$new_volume" != "$current_volume" ]; then
       paplay /usr/share/sounds/freedesktop/stereo/audio-volume-change.oga  # Replace with the path to your sound file
        current_volume=$new_volume
    fi

    # Adjust the sleep duration according to your needs
    sleep 0
done



