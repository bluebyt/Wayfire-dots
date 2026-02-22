#!/bin/bash

# Here we set the Bluetooth device address
device_address="60:93:16:0D:F9:59"

# Get the connection status of the device
connection_status=$(echo -e "info $device_address" | bluetoothctl | grep "Connected:" | awk '{print $2}')

# Here we determine status based on connection status
if [ "$connection_status" == "yes" ]; then
  status="connected"
else
  status="disconnected"
fi

toggle_state () {
# If the device is connected, do nothing
if [ "$connection_status" == "yes" ]; then
  status="disconnected"
else
  # If the device is disconnected, connect to it
  status="connected"
  bluetoothctl << EOF
  connect $device_address
EOF
fi
}

status_str () {
# Check the status and print the corresponding icon
if [ "$status" == "connected" ]; then
    echo " "  # Icon for connected
elif [ "$status" == "disconnected" ]; then
    echo ""  # Icon for disconnected
fi
}

case "$1" in
    --toggle) 
        toggle_state
        ;;
    --status)
        status_str
        ;;
esac
