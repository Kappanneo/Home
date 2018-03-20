#!/bin/sh
mouse=$(xinput list --name-only | grep "Mouse")
xinput --set-prop "$mouse" 'Evdev Wheel Emulation' 1
xinput --set-prop "$mouse" 'Evdev Wheel Emulation Button' 2
xinput --set-prop "$mouse" 'Evdev Wheel Emulation Axes' 6 7 4 5
