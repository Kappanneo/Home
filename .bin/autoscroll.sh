#!/bin/sh

mouse=$(xinput list --name-only | grep "Mouse")
if [ $1 -eq "0" ]
then
    xinput --set-prop "$mouse" 'Evdev Wheel Emulation' 0
elif [ $1 -eq "1" ]
then
    xinput --set-prop "$mouse" 'Evdev Wheel Emulation' 1
    xinput --set-prop "$mouse" 'Evdev Wheel Emulation Button' 2
    xinput --set-prop "$mouse" 'Evdev Wheel Emulation Axes' 6 7 4 5
    xinput --set-prop "$mouse" 'Evdev Middle Button Timeout' 50
    xinput --set-prop "$mouse" 'Evdev Wheel Emulation Timeout' 100
elif [ $(xinput list-props "$mouse" | grep "Evdev Wheel Emulation (313)" | cut -d ':' -f2) -eq "1" ]
then
    xinput --set-prop "$mouse" 'Evdev Wheel Emulation' 0
else
    xinput --set-prop "$mouse" 'Evdev Wheel Emulation' 1
    xinput --set-prop "$mouse" 'Evdev Wheel Emulation Button' 2
    xinput --set-prop "$mouse" 'Evdev Wheel Emulation Axes' 6 7 4 5
    xinput --set-prop "$mouse" 'Evdev Middle Button Timeout' 50
    xinput --set-prop "$mouse" 'Evdev Wheel Emulation Timeout' 100
fi


