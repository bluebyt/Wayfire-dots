#!/bin/bash

# Get the active workspace number
active_ws=$(~/.config/ipc-scripts/active_workspace_number.py)

# Construct the JSON output
jq --null-input --unbuffered --compact-output \
    --arg text "$active_ws" \
    --arg class "active$active_ws" \
    '{text: $text, class: $class}'
