#! /usr/bin/bash
if [[ -f "/tmp/br"  ]]; then
    BRIGHTNESS=`cat /tmp/br`
else
    echo -n "0" >> /tmp/br
    BRIGHTNESS=0
fi


if [[ $1 -eq 1 ]]; then
    BRIGHTNESS=$((BRIGHTNESS+1))
else
    BRIGHTNESS=$((BRIGHTNESS-1))
fi

echo -n $BRIGHTNESS > /tmp/br
xset r rate 150 40
rogauracore brightness $BRIGHTNESS
# Some wierd bug when brightness is changed xset is reset
xset r rate 150 40
