#include "arrows.py"
#begin python

MODES = {

"$pow":
    ('"POWER: [q]uit  [r]estart  [s]uspend  [h]ibernate  [esc]"',
     ['XF86PowerOff'], # to disable standard poweroff: in /etc/systemd/logind.conf (M-c M-q) set HandlePowerKey=ignore
     "mode $pow",
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
     "",
     [],
     []),

"$wrt":
    ('"WRITE: writing enabled"',
     ['Return','BackSpace','space','Delete','"Alt_L"'],
     "mode $def",
     "$exec $alert $wrt",
     "",
     [],
     "",
     "",
     [],
     []),

"$tch":
    ('"TOUCH: touchpad enabled  [space|esc] write mode"',
     ['Mod4+space'],
     "mode $tch",
     "$exec $alert $tch & $touchpad_on",
     "$exec $touchpad_off",
     [],
     "",
     "",
     ARROWS["default"]+['"Control_L"','"Control_R"','"Alt_L"','"Shift_L"','"Shift_R"',"Tab"],
     ARROWS["default"]),

"$hov":
    ('"HOVER: writing disabled  [oklò] move cursor  [0] insert  [space|esc] write mode"',
     ['Mod1+Menu','Menu'],
     "mode $hov",
     "$exec $alert $hov & $oklò_enable",
     "$exec $oklò_disable",
     [],
     "",
     "",
     ARROWS["default"]+['"Control_L"','"Control_R"','"Alt_L"','space','"Shift_L"','"Shift_R"',"Return","Tab","Menu"],
     ARROWS["default"]),

"$str":
    ('"START: [1|2] layouts  [spaec|esc] exit mode"',
     ['Mod4+z'],
     "mode $str",
     "$exec $alert $str",
     "",
    [    
         ("1",'$exec "$layout_1; $fill_1"'),
         ("2",'$exec "$layout_2; $fill_2"'),
         ("3",'$exec "$layout_3; $fill_3"'),
     ],
     "$wrt",
     "Mod4",
     [],
     []),

"$red":
    ('"REDSH: [123] shift red level  [+] increase  [space|esc] exit mode"',
     ['Mod4+r'],
     "mode $red",
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
     "Mod4",
     [],
     []),

"$cnf":
    ('"CONFG: [c]onfigure i3  [a]pplications  status[b]ar  [e]macs  [g]uide  [1-2|l]ayouts  [p]amac  [r]edshift  [s]ystemd  [z]sh  [space|esc] exit mode"',
     ['Mod4+c'],
     "mode $cnf",
     "$exec $alert $cnf",
     "",
     [    
         ("a","$exec $emacs /sudo::/usr/share/applications/"),
         ("b","$exec $emacs ~/.config/i3status/config"),
         ("c","$exec $emacs ~/.i3/"),
         ("e","$exec $emacs ~/.emacs"),
         ("g","$exec chromium --new-window i3wm.org/docs/userguide.html"),
         ("l","$exec $emacs ~/.workspaces/stamp.json"),
         ("p","$exec $emacs /sudo::/etc/pamac.conf"),
         ("r","$exec $emacs ~/.config/redshift/redshift.conf"),
         ("s","$exec $emacs /sudo::/etc/systemd/"),
         ("z","$exec $emacs ~/.zshrc"),
         ("1","$exec $emacs ~/.workspaces/$w1.json"),
         ("2","$exec $emacs ~/.workspaces/$w2.json"),
     ],
     "$wrt",
     "Mod4",
     [],
     [])

}

#end python
