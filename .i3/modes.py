#include "merge.py"
#begin python

MODES = {

"$pow":
    ('"POWER: [q]uit  [r]estart  [s]uspend  [h]ibernate  [esc]"',
     ['XF86PowerOff'], # to disable standard poweroff: in /etc/systemd/logind.conf set HandlePowerKey=ignore
     "$no_border mode $pow",
     "$exec $alert $pow, fullscreen disable",
     "",
     [
         ("XF86PowerOff","$exec $alert $pow"),
         ("q","$exec systemctl poweroff"),
         ("r","$exec systemctl reboot"),
         ("s","$exec systemctl suspend"),
         ("h","$exec systemctl hibernate")
     ],
     "$wrt",
     []),

"$wrt":
    ('"WRITE: writing enabled"',
     ['BackSpace','space'],
     "$no_border mode $def",
     "$exec $alert $wrt & $oklò_disable",
     "$exec $oklò_enable",
     [],
     "",
     []),

"$tch":
    ('"TOUCH: touchpad enabled  [space|esc] write mode"',
     ['Mod4+space'],
     "$no_border mode $tch",
     "$exec $alert $tch & $touchpad_on",
     "$exec $touchpad_off",
     [],
     "",
     ['"Control_L"']),

"$sup":
    ('"SUPER: [oklò] select  [shift+] move  [123] workspace  [Menu] hover mode  [super+space] touch mode  [space|esc] write mode"',
     ['--release "Super_L"'],
     "$border mode $sup",
     "$exec $alert $sup, $focus_one fullscreen disable",
     "",
     [],
     "",
     []),

"$hov":
    ('"HOVER: writing disabled  [oklò] move cursor  [0] insert  [space|esc] write mode"',
     ['Menu'],
     "$no_border mode $hov",
     "$exec $alert $hov",
     "",
     [],
     "",
     [])
} 

SUBMODES = {

"$str":
    ('"START: [1|2] layouts  [space|esc] exit mode"',
     'z',
     "$no_border mode $str",
     "$exec $alert $str",
     "",
    [    
         ("1",'$exec "$layout_1; $fill_1"'),
         ("2",'$exec "$layout_2; $fill_2"'),
     ],
     "$wrt",
     []),

"$red":
    ('"REDSH: [123] shift red level  [+] increase  [space|esc] exit mode"',
     'r',
     "$no_border mode $red",
     "$exec $alert $red",
     "",
     [    
         ("1","$exec redshift -P -O 2100K"),
         ("2","$exec redshift -P -O 2300K"),
         ("3","$exec redshift -P -O 2500K"),
         ("4","$exec redshift -P -O 2700K"),
         ("5","$exec redshift -P -O 3000K"),
         ("6","$exec redshift -P -O 3500K"),
         ("7","$exec redshift -P -O 4000K"),
         ("8","$exec redshift -P -O 4500K"),
         ("9","$exec redshift -P -O 5000K"),
         ("0","$exec redshift -P -O 6500K"),
         ("plus","$exec redshift -O 6400K")
     ],
     "",
     []),

"$cnf":
    ('"CONFG: [c]onfigure i3  .git[i]gnore  [a]pplications  [e]macs  [s]tatusbar  [z]sh  [g]uide  [1|2|l]ayouts  [r]edshift  [space|esc] exit mode"',
     'c',
     "$no_border mode $cnf",
     "$exec $alert $cnf",
     "",
     [    
         ("c","$exec $emacs ~/.i3/index.conf"),                                  
         ("Shift+c","$exec $emacs ~/.i3/modes.py"),
         ("i","$exec $emacs ~/.gitignore"),
         ("a","$exec $emacs /sudo::/usr/share/applications/"),
         ("e","$exec $emacs ~/.emacs"),
         ("s","$exec $emacs ~/.config/i3status/config"),
         ("z","$exec $emacs ~/.zshrc"),
         ("g","$exec chromium --new-window i3wm.org/docs/userguide.html"),
         ("l","$exec $emacs ~/.workspaces/stamp.json"),
         ("1","$exec $emacs ~/.workspaces/$w1.json"),
         ("2","$exec $emacs ~/.workspaces/$w2.json"),
         ("r","$exec $emacs ~/.config/redshift/redshift.conf")
     ],
     "$wrt",
     [])

}

ALLMODES = merge(MODES,SUBMODES)

#end python
