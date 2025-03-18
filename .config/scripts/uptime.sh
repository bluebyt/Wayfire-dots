#!/bin/bash
awk '{m=$1/60; h=m/60; printf "%sd %sh %sm", int(h/24), int(h%24), int(m%60) }' /proc/uptime
