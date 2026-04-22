#!/usr/bin/env expect

# Set the MAC address
set mac "60:93:16:0D:F9:59"

# How long to wait for each 'expect' match (in seconds)
set timeout 30

# Start bluetoothctl
spawn bluetoothctl

# 1. Power on
send -- "power on\r"
sleep 1

# 2. Scan on
send -- "scan on\r"
sleep 1

# 3. Remove the existing profile (Cleans up stale Arch configs)
send -- "remove $mac\r"
expect "Device has been removed"

# 4. Prompt the user
send_user "\n\n!!! PUSH THE BUTTON NOW (FLASHING WHITE) !!!\n\n"

# 5. Wait for the device to appear in the scan
# This is better than 'sleep 12' because it proceeds the moment it's found
expect "$mac"

# 6. Pair
send -- "pair $mac\r"
expect "Pairing successful"

# 7. Trust
send -- "trust $mac\r"
expect "trust succeeded"

# 8. Connect
send -- "connect $mac\r"
expect "Connection successful"

# 9. Quit
send -- "quit\r"
expect eof
