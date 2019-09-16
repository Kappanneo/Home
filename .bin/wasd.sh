#!/bin/sh
if [ $1 -eq "0" ]
then
    xmodmap -e "keycode  25 = w W w W lstroke Lstroke lstroke Lstroke w W lstroke Lstroke"
    xmodmap -e "keycode  38 = a A a A ae AE ae AE a A ae AE"
    xmodmap -e "keycode  39 = s S s S ssharp section ssharp section s S ssharp section"
    xmodmap -e "keycode  40 = d D d D eth ETH eth ETH d D eth ETH"

    xmodmap -e "keycode  26 = e E e E EuroSign cent EuroSign cent e E EuroSign cent"

elif [ $1 -eq "1" ]
then
    xmodmap -e "keycode  25 = Up Up Up"
    xmodmap -e "keycode  38 = Left Left Left"
    xmodmap -e "keycode  39 = Down Down Down"
    xmodmap -e "keycode  40 = Right Right Right"

    xmodmap -e "keycode  26 = Return NoSymbol Return NoSymbol Return"

fi
