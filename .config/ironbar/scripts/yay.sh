#!/bin/bash

# Run the yay command to list available updates and count the lines
update_count=$(yay -Qu | wc -l)

# Output the number of available updates
echo "$update_count"
