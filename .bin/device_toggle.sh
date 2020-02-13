#!/bin/sh
device=$(xinput list --name-only | grep -i $1)
if [ $2 -eq "0" ]
then
    xinput set-prop "$device" "Device Enabled" 0
elif [ $2 -eq "1" ]
then
    xinput set-prop "$device" "Device Enabled" 1
elif [ $(xinput list-props "$device" | grep "Device Enabled" | cut -d ':' -f2) -eq "1" ]
then
    xinput set-prop "$device" "Device Enabled" 0
else
    xinput set-prop "$device" "Device Enabled" 1
fi
