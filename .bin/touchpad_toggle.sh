#!/bin/sh
touchpad=$(xinput list --name-only | grep "Touchpad")
if [ $1 -eq "0" ]
then
    xinput set-prop "$touchpad" "Device Enabled" 0
elif [ $1 -eq "1" ]
then
    xinput set-prop "$touchpad" "Device Enabled" 1
elif [ $(xinput list-props "$touchpad" | grep "Device Enabled" | cut -d ':' -f2) -eq "1" ]
then
    xinput set-prop "$touchpad" "Device Enabled" 0
else
    xinput set-prop "$touchpad" "Device Enabled" 1
fi
