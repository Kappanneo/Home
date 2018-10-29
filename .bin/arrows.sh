#!/bin/sh
if [ $1 -eq "0" ]
then
    xmodmap -e "keycode  32 = o O o O oslash Oslash oslash"
    xmodmap -e "keycode  45 = k K k K kra ampersand kra"
    xmodmap -e "keycode  46 = l L l L lstroke Lstroke lstroke"
    xmodmap -e "keycode  47 = ograve ccedilla ograve ccedilla at dead_cedilla at"
    xmodmap -e "keycode  33 = p P p P thorn THORN thorn"
    xmodmap -e "keycode  31 = i I i I rightarrow idotless rightarrow"
  
elif [ $1 -eq "1" ]
then
    xmodmap -e "keycode  32 = Up"
    xmodmap -e "keycode  45 = Left"
    xmodmap -e "keycode  46 = Down"
    xmodmap -e "keycode  47 = Right"
    xmodmap -e "keycode  33 = End"
    xmodmap -e "keycode  31 = Home"
fi
