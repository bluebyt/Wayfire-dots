#!/usr/bin/env bash
sleep 1
killall xdg-desktop-portal xdg-desktop-portal-wlr xdg-desktop-portal-hyprland
systemctl --user restart xdg-desktop-portal-wlr

