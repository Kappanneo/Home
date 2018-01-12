#!/bin/sh
i3status | while :
do
    read line
    id=$(xprop -root | awk '/_NET_ACTIVE_WINDOW\(WINDOW\)/{print $NF}')
    name=$(xprop -id $id | awk '/\<WM_NAME/{print}' | cut -d'"' -f2)
    echo "$name | $line" || exit 1
done
