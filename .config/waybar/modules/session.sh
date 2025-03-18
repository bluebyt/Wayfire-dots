#!/bin/sh

uptime=$(uptime | awk -F, '{sub(".*up ",x,$1);print $1}')
echo $uptime
