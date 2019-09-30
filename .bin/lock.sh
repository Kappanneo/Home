#!/usr/bin/env bash

# reset default
/home/claudio/.bin/oklò.sh 0
/home/claudio/.bin/touchpad_toggle.sh 1
i3-msg mode default
notify-send default

# set the icon and a temporary location for the screenshot to be stored
tmpbg='/tmp/screen.png'

# take a screenshot
scrot -o "$tmpbg"

# blur the screenshot by resizing and scaling back up
convert "$tmpbg" -filter Gaussian -thumbnail 20% -sample 500% "$tmpbg"

# lock the screen with the blurred screenshot
i3lock -ui "$tmpbg"
