#!/bin/bash

SERVICE="xava"

while true; do

if pgrep -x "$SERVICE" >/dev/null
then
    echo "$SERVICE is running"
else
    echo "$SERVICE stopped"
    /usr/bin/xava &
fi
sleep 5
done
