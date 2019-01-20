#!/bin/sh
i3status | while :
do
    read line
    id=$(xprop -root | awk '/_NET_ACTIVE_WINDOW\(WINDOW\)/{print $NF}')
    name=$(xprop -len 30 -id $id | awk '/\<WM_NAME/{print}' | cut -d'=' -f2 | cut -d'"' -f2)
    class=$(xprop -len 30 -id $id | awk '/\<WM_CLASS/{print}' | cut -d'=' -f2 | cut -d'"' -f2)
    echo "$name | $class | $line" || exit 1
done
