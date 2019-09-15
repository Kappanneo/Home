#include "arrows.py"
#begin python

MODES = {

"$def":
    ('"default"',
     ['Mod4+q'],
     "",
     "$touchpad_on",
     "",
     [],
     "",
     "",
     [],
     []),

"$pow":
    ('"POWER: [q]uit  [r]estart  [s]uspend  [h]ibernate  [esc]"',
     ['XF86PowerOff'], # to disable standard poweroff: in /etc/systemd/logind.conf (M-c M-q) set HandlePowerKey=ignore
     "fullscreen disable",
     "",
     "",
     [
         ("q","$exec systemctl poweroff"),
         ("r","$exec systemctl reboot"),
         ("s","$exec systemctl suspend"),
         ("h","$exec systemctl hibernate"),
         ("Escape",""),
     ],
     "$def",
     "",
     [],
     []),

"$wrt":
    ('"WRITE: [super] super mode"',
     [],
     "",
     "$touchpad_x_off",
     "",
     [],
     "",
     "",
     [],
     []),

"$tch":
    ('"TOUCH: [super] super mode"',
     [],
     "",
     "$touchpad_x_on",
     "$touchpad_x_off",
     [
         ('"Super_L"',""),
     ],
     "$sup",
     "",
     ['"Control_L"','"Control_R"','"Alt_L"'],
     []),

"$sup":
    ('"SUPER: [super+q] exit super mode  [oklò] arrows  [j-à] home-end  [i-p] page up-down  [alt_gr] escape  [backspace] write  [super+c] config  [super+r] redshift  [super+z] layouts"',
     ['--release "Super_L"','Menu'],
     "",
     "$oklò_enable && $touchpad_x_off",
     "$oklò_disable",
     [],
     "",
     "",
     ARROWS["default"]+['"Control_L"','"Control_R"','"Alt_L"','space','"Shift_L"','"Shift_R"',"Return","Tab","Menu"],
     ARROWS["default"]),

"$str":
    ('"START: [super+] [1-2] layouts"',
     ['Mod4+z'],
     "",
     "",
     "",
     [
         ("1",'$exec "$layout_1; $fill_1"'),
         ("2",'$exec "$layout_2; $fill_2"'),
     ],
     "$sup",
     "Mod4",
     [],
     []),

"$red":
    ('"REDSH: [super+] [0-9] one shot red shift  [+] increase"',
     ['Mod4+r'],
     "",
     "",
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
         ("plus","$exec redshift -O 6400K"),
     ],
     "",
     "Mod4",
     [],
     []),

"$brg":
    ('"BRGHT: [super+] [0-9] set brightness level  [+] increase  [-] decrease"',
     ['Mod4+b'],
     "",
     "",
     "",
     [
         ("1","$exec xbacklight = 10"),
         ("2","$exec xbacklight = 20"),
         ("3","$exec xbacklight = 30"),
         ("4","$exec xbacklight = 40"),
         ("5","$exec xbacklight = 50"),
         ("6","$exec xbacklight = 60"),
         ("7","$exec xbacklight = 70"),
         ("8","$exec xbacklight = 80"),
         ("9","$exec xbacklight = 90"),
         ("0","$exec xbacklight = 100"),
         ("plus","$exec xbacklight +5"),
         ("minus","$exec xbacklight -5"),
     ],
     "",
     "Mod4",
     [],
     []),

"$cnf":
    ('"CONFG: [super+] [c]onfigure i3  [a]pplications  status[b]ar  [e]macs  [g]uide  [1-2|l]ayouts  [p]amac  [r]edshift  [s]ystemd  [z]sh"',
     ['Mod4+c'],
     "",
     "",
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
     "$sup",
     "Mod4",
     [],
     [])

}

#end python
