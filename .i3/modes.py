#include "arrows.py"
#begin python

MODES = {

"$def":
    ('"default"',
     ["Mod4+q"],
     {
         "exec_on_enter":"$touchpad_on",
     }),

"$wrt":
    ('"WRITE: [super+q] quit mode"',
     [],
     {
         "exec_on_enter":"$touchpad_x_off",
     }),

"$rgh":
     ('"RIGHT: [oklò] arrows  [j-à] home-end  [i-p] page up-down  [alt_gr] escape  [backspace] write  [super+q] quit mode"',
      ['--release Super_R'],
      {
          "exec_on_enter":"$oklò_enable && $touchpad_x_off",
          "exec_on_exit":"$oklò_disable",
      }),

"$lft":
     ('"LEFT: [wasd] arrows  [e] enter  [super+q] quit mode"',
      ['--release "Super_L"'],
      {
          "exec_on_enter":"$wasd_enable && $touchpad_x_off",
          "exec_on_exit":"$wasd_disable",
      }),

"$pow":
    ('"POWER: [q]uit  [r]estart  [s]uspend  [h]ibernate  [esc]"',
     ['XF86PowerOff'], # to disable standard poweroff: in /etc/systemd/logind.conf (M-c M-q) set HandlePowerKey=ignore
     {
         "options":[
             ("q","$exec systemctl poweroff"),
             ("r","$exec systemctl reboot"),
             ("s","$exec systemctl suspend"),
             ("h","$exec systemctl hibernate"),
             #("Escape",""),
         ],

         "after_mode":"$def",
     }),

"$str":
    ('"START: [super+] [1-2] layouts"',
     ['Mod4+z'],
     {
         "options":[
             ("Mod4+1",'$exec "$layout_1; $fill_1"'),
             ("Mod4+2",'$exec "$layout_2; $fill_2"'),
         ],

         "after_mode":"$def",
     }),

"$red":
     ('"REDSH: [super+] [0-9] one shot red shift  [+] increase  [q] quit"',
      ['Mod4+r'],
      {
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
      }),

"$brg":
     ('"BRGHT: [super+] [0-9] set brightness level  [+] increase  [-] decrease  [q] quit"',
      ['Mod4+b'],
      {
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
      }),

"$cnf":
     ('"CONFG: [super+] [c]onfigure i3  [a]pplications  status[b]ar  [e]macs  [g]uide  [1-2|l]ayouts  [p]amac  [r]edshift  [s]ystemd  [z]sh  [q] quit"',
      ['Mod4+c'],
      {
          "options":[
              ("Mod4+c","$exec $emacs ~/.i3/"),
              ("Mod4+a","$exec $emacs /sudo::/usr/share/applications/"),
              ("Mod4+b","$exec $emacs ~/.config/i3status/config"),
              ("Mod4+e","$exec $emacs ~/.emacs"),
              ("Mod4+g","$exec chromium --new-window i3wm.org/docs/userguide.html"),
              ("Mod4+l","$exec $emacs ~/.workspaces/stamp.json"),
              ("Mod4+p","$exec $emacs /sudo::/etc/pamac.conf"),
              ("Mod4+r","$exec $emacs ~/.config/redshift/redshift.conf"),
              ("Mod4+s","$exec $emacs /sudo::/etc/systemd/"),
              ("Mod4+z","$exec $emacs ~/.zshrc"),
              ("Mod4+1","$exec $emacs ~/.workspaces/$w1.json"),
              ("Mod4+2","$exec $emacs ~/.workspaces/$w2.json"),
          ],
          "after_mode":"$def",
      }),

}

#end python
