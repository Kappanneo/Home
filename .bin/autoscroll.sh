#!/bin/sh
mouse=$(xinput list --name-only | grep "Mouse")
if [ $1 -eq "0" ]
then
    xinput --set-prop "$mouse" "libinput Scroll Method Enabled" 0, 0, 0
elif [ $1 -eq "1" ]
then
    xinput --set-prop "$mouse" "libinput Scroll Method Enabled" 0, 0, 1
    xinput --set-prop "$mouse" "libinput Button Scrolling Button" 2
fi
