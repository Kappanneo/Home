#!/bin/sh
if [ $1 -eq "0" ]
then
    xmodmap -e "keycode  32 = o O o O oslash Oslash oslash"
    xmodmap -e "keycode  45 = k K k K kra ampersand kra"
    xmodmap -e "keycode  46 = l L l L lstroke Lstroke lstroke"
    xmodmap -e "keycode  47 = ograve ccedilla ograve ccedilla at dead_cedilla at"

    xmodmap -e "keycode  33 = p P p P thorn THORN thorn"
    xmodmap -e "keycode  31 = i I i I rightarrow idotless rightarrow"
    xmodmap -e "keycode  44 = j J j J dead_hook dead_horn dead_hook dead_horn"
    xmodmap -e "keycode  48 = agrave degree agrave degree numbersign dead_abovering numbersign dead_abovering agrave degree numbersign dead_abovering"
elif [ $1 -eq "1" ]
then
    xmodmap -e "keycode  32 = Up Up Up"
    xmodmap -e "keycode  45 = Left Left Left"
    xmodmap -e "keycode  46 = Down Down Down"
    xmodmap -e "keycode  47 = Right Right Right"

    xmodmap -e "keycode  48 = End End End"
    xmodmap -e "keycode  44 = Home Home Home"
    xmodmap -e "keycode  31 = Prior NoSymbol Prior NoSymbol Prior"
    xmodmap -e "keycode  33 = Next NoSymbol Next NoSymbol Next"
fi
