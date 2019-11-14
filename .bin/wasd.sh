#!/bin/sh
if [ $1 -eq "0" ]
then
    xmodmap -e "keycode  25 = w W w W lstroke Lstroke lstroke Lstroke w W lstroke Lstroke"
    xmodmap -e "keycode  38 = a A a A ae AE ae AE a A ae AE"
    xmodmap -e "keycode  39 = s S s S ssharp section ssharp section s S ssharp section"
    xmodmap -e "keycode  40 = d D d D eth ETH eth ETH d D eth ETH"

    xmodmap -e "keycode  94 = less greater less greater guillemotleft guillemotright guillemotleft guillemotright less greater guillemotleft guillemotright"
    xmodmap -e "keycode  41 = f F f F dstroke ordfeminine dstroke ordfeminine f F dstroke ordfeminine"

    xmodmap -e "keycode  24 = q Q q Q at Greek_OMEGA at Greek_OMEGA q Q at Greek_OMEGA"
    xmodmap -e "keycode  26 = e E e E EuroSign cent EuroSign cent e E EuroSign cent"

    xmodmap -e "keycode  52 = z Z z Z guillemotleft less guillemotleft less z Z guillemotleft less"
    xmodmap -e "keycode  53 = x X x X guillemotright greater guillemotright greater x X guillemotright greater"

    xmodmap -e "keycode  27 = r R r R paragraph registered paragraph registered r R paragraph registered"
    xmodmap -e "keycode  54 = c C c C cent copyright cent copyright c C cent copyright"

elif [ $1 -eq "1" ]
then
    xmodmap -e "keycode  25 = Up Up Up"
    xmodmap -e "keycode  38 = Left Left Left"
    xmodmap -e "keycode  39 = Down Down Down"
    xmodmap -e "keycode  40 = Right Right Right"

    xmodmap -e "keycode  94 = Home Home Home"
    xmodmap -e "keycode  41 = End End End"

    xmodmap -e "keycode  24 = Prior NoSymbol Prior NoSymbol Prior"
    xmodmap -e "keycode  26 = Next NoSymbol Next NoSymbol Next"

    xmodmap -e "keycode  52 = Menu NoSymbol Menu NoSymbol Menu"
    xmodmap -e "keycode  53 = Escape NoSymbol Escape NoSymbol Escape"

    xmodmap -e "keycode  27 = Return NoSymbol Return NoSymbol Return"
    xmodmap -e "keycode  54 = BackSpace Delete BackSpace BackSpace NoSymbol NoSymbol Terminate_Server NoSymbol NoSymbol Terminate_Server BackSpace BackSpace NoSymbol NoSymbol Terminate_Server"
fi
