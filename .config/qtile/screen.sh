#!/bin/sh
if [[ ! -e /tmp/screen ]]; then
    xrandr --output eDP-1 --primary --mode 1920x1080 --pos 0x0 --rotate normal --output DP-1-0 --off --output DP-1-1 --off --output HDMI-1-0 --mode 1920x1080 --pos 1920x0 --rotate normal
    feh --bg-fill /home/avenortoz/Pictures/test_2.png
    touch /tmp/screen
else
    xrandr --output eDP-1 --primary --mode 1920x1080 --pos 0x0 --rotate normal --output DP-1-0 --off --output DP-1-1 --off --output HDMI-1-0 --off
    rm /tmp/screen
fi
