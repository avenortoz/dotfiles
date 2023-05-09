#!/bin/bash
feh --bg-scale "${HOME}/Pictures/leader.png"
xset r rate 250 40
setxkbmap -layout us,ua -option 'grp:alt_shift_toggle'
picom -b
mpd
redshift -l 49.5538888:25.6091666 &
nohup greenclip daemon &
comm.sh &
xfce4-power-manager --daemon
# picom -b --experimental-backends --backend glx
comm.sh
