#!/usr/bin/env bash

# CHANGE THIS to the mount point (NOT the block device)
MOUNT="/"

read -r total used avail percent <<<$(df -B1 --output=size,used,avail,pcent "$MOUNT" | tail -n 1)

# Safety check
if [ -z "$total" ] || [ "$total" -eq 0 ]; then
  echo "disk N/A"
  exit 0
fi

# Convert bytes → GB
total_gb=$(( total / 1024 / 1024 / 1024 ))
used_gb=$(( used / 1024 / 1024 / 1024 ))

avail_pct=$(awk "BEGIN { printf \"%.2f\", ($avail/$total)*100 }")

echo "Used: ${used_gb}GB / ${total_gb}GB
Available: ${avail_pct}%"

