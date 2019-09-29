#!/usr/bin/env bash

# location of the screenshot for startup lockscreen
tmpbg='/home/claudio/Pictures/Screenshots/startup_lockscreen.png'

# take a screenshot
scrot -o "$tmpbg"

# blur the screenshot by resizing and scaling back up
convert "$tmpbg" -filter Gaussian -thumbnail 20% -sample 500% "$tmpbg"
