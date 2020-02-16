#include "arrows.py"
#begin python

MODES = {

"$sup": {
    "name":'"SUPER"',
    "keys":['"Super_L"','"Super_R"'],
},

"$pow": {
    "name":'"POWER: [q] power off  [r]estart  [s]uspend  [h]ibernate  [x] turn off screen  [l]ock  [esc] do nothing"',
    "keys":['XF86PowerOff'], # to disable standard poweroff: in /etc/systemd/logind.conf set HandlePowerKey=ignore
    "options":[
        ("q","$exec systemctl poweroff"),
        ("r","$exec systemctl reboot"),
        ("s","$exec systemctl suspend"), # auto locks via service: write /etc/systemd/system/lock.service (https://gist.github.com/Kappanneo/8a9da9e6d23b9f38bc7cf33eb071cca5)
        ("h","$exec systemctl hibernate"), # also auto locks
        ("x","$exec $lock && $screen_off"),
        ("l","$exec $lock"), # lock script sets the defaut mode and keybinding: (.bin/lock.sh)
    ],
    "on_enter":"fullscreen disable",
},

"$wrt": {
    "name":'"default"',
    "keys":['control+"Alt_L"',"control+$alt_gr","Mod1+$alt_gr"],
    "exec_on_enter":"$mouse_off && $touchpad_off && $pointer_hide",
},

"$lft": {
    "name":'"LEFT: [wasd] arrows  [q-e] page up-down  [r]eturn  [z] menu  [x] escape"',
    "keys":['control+"Super_L"'],
    "exec_on_enter":"$wasd_enable",
    "exec_on_exit":"$wasd_disable",
},

"$rgh": {
    "name":'"RIGHT: [oklò] arrows  [j-à] home-end  [i-p] page up-down  [period] menu  [comma] escape"',
    "keys":['control+"Super_R"','Mod4+"Super_R"'],
    "exec_on_enter":"$oklò_enable",
    "exec_on_exit":"$oklò_disable",
},

"$str": {
    "name":'"START: [super+] [1-2] layouts [u]pdate startup lockscreen"',
    "keys":['Mod4+backslash'],
    "options":[
        ("Mod4+1",'$exec "$layout_1; $fill_1"'),
        ("Mod4+2",'$exec "$layout_2; $fill_2"'),
        ("Mod4+u",'$exec "$layout_2; $fill_2; sleep 1.6; $update_startup_lockscreen"')
        ],
    "after_mode":"$wrt",
},

"$red": {
    "name":'"REDSH: [super+] [0-9] one shot red shift  [+] increase"',
    "keys":['Mod4+r'],
    "options":[
        ("Mod4+1","$exec redshift -P -O 2100K"),
        ("Mod4+2","$exec redshift -P -O 2300K"),
        ("Mod4+3","$exec redshift -P -O 2500K"),
        ("Mod4+4","$exec redshift -P -O 2700K"),
        ("Mod4+5","$exec redshift -P -O 3000K"),
        ("Mod4+6","$exec redshift -P -O 3500K"),
        ("Mod4+7","$exec redshift -P -O 4000K"),
        ("Mod4+8","$exec redshift -P -O 4500K"),
        ("Mod4+9","$exec redshift -P -O 5000K"),
        ("Mod4+0","$exec redshift -P -O 6500K"),
        ("Mod4+plus","$exec redshift -O 6400K"),
    ],
},

"$brg": {
    "name":'"BRGHT: [super+] [0-9] set brightness level  [+] increase  [-] decrease"',
    "keys":['Mod4+b'],
    "options":[
        ("Mod4+1","$exec xbacklight = 10"),
        ("Mod4+2","$exec xbacklight = 20"),
        ("Mod4+3","$exec xbacklight = 30"),
        ("Mod4+4","$exec xbacklight = 40"),
        ("Mod4+5","$exec xbacklight = 50"),
        ("Mod4+6","$exec xbacklight = 60"),
        ("Mod4+7","$exec xbacklight = 70"),
        ("Mod4+8","$exec xbacklight = 80"),
        ("Mod4+9","$exec xbacklight = 90"),
        ("Mod4+0","$exec xbacklight = 100"),
        ("Mod4+plus","$exec xbacklight +5"),
        ("Mod4+minus","$exec xbacklight -5"),
    ],
},

"$cnf": {
    "name":'"CONFG: [super+] [c]onfig  [a]pps  gru[b]  [e]macs  [g]uide  [1-2|l]ayouts  [p]amac  [r]edshift  [s]ystemd  [z]sh"',
    "keys":['Mod4+c'],
    "options":[
        ("Mod4+c","$exec $emacs ~/.i3/"),
        ("Mod4+a","$exec $emacs /sudo::/usr/share/applications/"),
        ("Mod4+b","$exec $emacs /sudo::/etc/default/grub"),
        ("Mod4+e","$exec $emacs ~/.emacs"),
        ("Mod4+g","$exec chromium --new-window i3wm.org/docs/userguide.html"),
        ("Mod4+l","$exec $emacs ~/.workspaces/stamp.json"),
        ("Mod4+p","$exec $emacs /sudo::/etc/pamac.conf"),
        ("Mod4+r","$exec $emacs ~/.config/redshift/redshift.conf"),
        ("Mod4+s","$exec $emacs /sudo::/etc/systemd/"),
        ("Mod4+z","$exec $emacs ~/.zshrc"),
        ("Mod4+1","$exec $emacs ~/.workspaces/1.json"),
        ("Mod4+2","$exec $emacs ~/.workspaces/2.json"),
    ],
    "after_mode":"$wrt",
},

"$tmp": {
    "name":'"STAMP: [super+] [t]ake screenshot [w]indow [s]elect [o]pen screenshot folder"',
    "keys":['Mod4+t'],
    "options":[
        ("Mod4+t","$exec i3-scrot"),
        ("Mod4+w","$exec i3-scrot -w"),
        ("--release Mod4+s","$exec i3-scrot -s"),
        ("Mod4+o","$exec $fm ~/Pictures/Screenshots"),
    ],
}

}

#end python
