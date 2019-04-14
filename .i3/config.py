#begin python

def merge(x, y):
    z = x.copy()   # start with x's keys and values
    z.update(y)    # modifies z with y's keys and values & returns None
    return z

def SET(d):
    string=""
    k = d.keys()
    k.sort()
    for x in k:
        t = d[x]
        string += "set {} {}\n".format(x,t[0])
    return string

def BINDALL(blocks,modifier,postfix,prefix,mode_tag):
    string = ""
    for name in blocks:
        string += " # {}\n".format(name)
        x = blocks[name]
        if type(x) == tuple:
            string += BIND(x,modifier,postfix,prefix,mode_tag)
        elif type(x) == list:
            for t in x:
                string += BIND(t,modifier,postfix,prefix,mode_tag)
        string += "\n"
    return string

def BIND(t,mod,post,pre,mode_tag):
    x,y = t
    if post != "" and y != "": y += "; " + post
    if post != "" and y == "": y += post
    if pre != "": y = pre + " " + y
    if mod != "": x = mod + "+" + x
    if mode_tag in USED_KEYS:
        if "Shift" in x: USED_KEYS[mode_tag].extend(['"Shift_L"','"Shift_R"'])
        if "control" in x : USED_KEYS[mode_tag].extend(['"Control_L"','"Control_R"'])
        USED_KEYS[mode_tag].append(x)
    return "bindsym {} {}\n".format(x,y)

def BINDALL_TO_MODE(blocks,mode_prev,mode_next):
    n, p, q, exit = ALLMODES[mode_prev]
    name, pre, post, e = ALLMODES[mode_next]
    if exit != "": post += "; " + exit
    return BINDALL(blocks,"",post,pre,mode_prev)

def BIND_TO_MODE(t,mode_prev,mode_next):
    n, p, q, exit = ALLMODES[mode_prev]
    name, pre, post, e = ALLMODES[mode_next]
    if exit != "": post += "; " + exit
    return BIND(t,"",post,pre,mode_prev)

def BEGIN_MODE(mode_tag):
    USED_KEYS[mode_tag] = []
    return "mode "+mode_tag+" {"

def END_MODE(mode_tag):
    USED = USED_KEYS[mode_tag]
    string = "";
    U = [(x,"nop") for x in KEYS if x not in USED]
    if len(U) :
        string += BINDALL({"unused keys":U},"","","","")
    if any([x for x in ['"Shift_L"','"Shift_R"'] if x in USED]):
        U = [(x,"nop") for x in ['Shift+'+y for y in SHIFT_KEYS] if x not in USED]
        string += BINDALL({"also Shift+ (since Shift is not locked)":U},"","","","")
    if any([x for x in ['"Control_L"','"Control_R"'] if x in USED]):
        U = [(x,"nop") for x in ['control+'+y for y in KEYS] if x not in USED]
        string += BINDALL({"also control+ (since control is not locked)":U},"","","","")
    return string + "\n}"

USED_KEYS ={}

KEYS = [
'Delete',
'backslash',
'1',
'2',
'3',
'4',
'5',
'6',
'7',
'8',
'9',
'0',
'aphostrophe',
'igrave',
'BackSpace',
'Tab',
'q',
'w',
'e',
'r',
't',
'y',
'u',
'i',
'o',
'p',
'egrave',
'plus',
'Return',
'Caps',
'a',
's',
'd',
'f',
'g',
'h',
'j',
'k',
'l',
'ograve',
'agrave',
'ugrave',
'"Shift_L"',
'less',
'z',
'x',
'c',
'v',
'b',
'n',
'm',
'comma',
'period',
'minus',
'"Shift_R"',
'"Control_L"',
'"Super_L"',
'"Alt_L"',
'space',
'$alt_gr',
'Menu',
'"Control_R"',
'Up',
'Left',
'Down',
'Right'
]

SHIFT_KEYS = [
'bar',
'exclam',
'quotedbl',
'sterling',
'dollar',
'percent',
'ampersand',
'slash',
'parenleft',
'parenright',
'equal',
'question',
'asciicircum',
'q',
'w',
'e',
'r',
't',
'y',
'u',
'i',
'o',
'p',
'eacute',
'asterisk',
'a',
's',
'd',
'f',
'g',
'h',
'j',
'k',
'l',
'ccedilla',
'degree',
'section',
'greater',
'z',
'x',
'c',
'v',
'b',
'n',
'm',
'semicolon',
'colon',
'underscore'
]

UNUSED_KEYS = []

#end python
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
 #                               SETTINGS                                      #
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

 # This font is widely installed, provides lots of unicode glyphs, right-to-left
 # text rendering and scalability on retina/hidpi displays (thanks to pango).
font pango:DejaVu Sans Mono 8

 # Use Mouse+Mod1 to drag floating windows to their wanted position
floating_modifier Mod1

 # no title-bars nor border
new_window pixel 0

 # no floating border
new_float pixel 0

 # go back to previous workspace if you try to go to the current one
 # (allow for fast window movement to a workspace and back)
workspace_auto_back_and_forth yes

 # focus on mouse (is a pain if you happen to have a mouse)
focus_follows_mouse no

 # I like the original snake better
focus_wrapping no

 # smart|ignore|leave_fullscreen
popup_during_fullscreen leave_fullscreen

 # smart|urgent|focus|none
focus_on_window_activation none

 # # # # # # # # # # # # # # # # # COLORS  # # # # # # # # # # # # # # # # # # #

 # class                 border  backgr. text    ind.    child
client.focused          #4CC97E #4CC97E #ffffff #4CC97E #4CC97E
client.focused_inactive #222222 #222222 #ffffff #222222 #222222
client.unfocused        #222222 #222222 #888888 #222222 #222222
client.urgent           #222222 #900000 #ffffff #900000 #900000
client.placeholder      #000000 #222222 #ffffff #000000 #222222

client.background       #222222

 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
 #                              DEFINITIONS                                    #
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

 # The (new) i3-dmenu-desktop which only displays applications
 # shipping a .desktop file. It is a wrapper around dmenu, so you need that
 # installed.
 # Since it's slow as **** someone made a fast one:
 # https://github.com/matteoalessiocarrara/k5-dmenu-desktop
set $dmenu i3-dmenu-desktop   # ~/k5-dmenu-desktop

 # file manager
set $fm nautilus -w

 # for brevity
set $exec exec --no-startup-id
set $exec_always exec_always --no-startup-id
set $alert notify-send --expire-time=1200
set $refresh_status_bar exec killall -USR1 i3status
set $focus_all focus parent; focus parent; focus parent; focus parent; focus parent; focus parent; focus parent; focus parent; focus parent; focus parent; focus parent; focus parent
set $focus_one focus child ; focus child ; focus child ; focus child ; focus child ; focus child ; focus child ; focus child ; focus child ; focus child ; focus child ; focus child
set $no_border [tiling] border none
set $border [tiling] border pixel 5
set $alt_gr "ISO_Level3_Shift"

 # # # # # # # # # # # # # # # # KEYBINDINGS # # # # # # # # # # # # # # # # # #

set $disable_Caps setxkbmap -option ctrl:nocaps
set  $enable_Caps setxkbmap -option
set $disable_hover_mode ~/.bin/hover.sh 0
set  $enable_hover_mode ~/.bin/hover.sh 1

 # # # # # # # # # # # # # # # FUNCTIONALITIES # # # # # # # # # # # # # # # # #

 # touchpad toggle
set $touchpad_on ~/.bin/touchpad_toggle.sh 1 & xdotool mousemove  750  350
set $touchpad_off ~/.bin/touchpad_toggle.sh 0 & xdotool mousemove 2500 1200
set $touchpad_off_2 ~/.bin/touchpad_toggle.sh 0
set $touchpad_toggle ~/.bin/touchpad_toggle.sh

 # autoscroll
set $disable_autoscroll ~/.bin/autoscroll.sh 0
set  $enable_autoscroll ~/.bin/autoscroll.sh 1

 # screenshot
set $stamp "import ~/Pictures/latest-screenshot.png; xdg-open ~/Pictures/latest-screenshot.png"

 # brightness
set $brightness_up exec "xbacklight -inc 5; notify-send 'brightness up'"
set $brightness_down exec "xbacklight -dec 5; notify-send 'brightness down'"

 # # # # # # # # # # # # # # # # WORKSPACES # # # # # # # # # # # # # # # # # # #
#begin python

WORKSPACES = {
"$w1":("1nternet", "1"),
"$w2":("2rectory", "2"),
"$w3":("3code",    "3"),
"$w4":("4terminl", "4"),
"$w5":("5team",    "5"),
"$w6":("6iscord",  "6"),
"$w7":("7atex",    "7"),
"$w8":("8volante", "8"),
"$w9":("9imp",     "9")
}

CUT_WORKSPACE = {
"$wx":("X",        "x")
}

ALLWORKSPACES = merge(WORKSPACES,CUT_WORKSPACE)
#end python

<[SET(WORKSPACES)]>
 # this one is for cut and paste
<[SET(CUT_WORKSPACE)]>
 # # # # # # # # # # # # # # # # LAYOUTS # # # # # # # # # # # # # # # # # # # #

set $layout_1 i3-msg 'workspace --no-auto-back-and-forth 1nternet; split h; focus parent; focus parent; focus parent; focus parent; kill; append_layout ~/.workspaces/1nternet.json'
set $layout_2 i3-msg 'workspace --no-auto-back-and-forth 2rectory; split h; focus parent; focus parent; focus parent; focus parent; focus parent; kill; append_layout ~/.workspaces/2rectory.json'

set $fill_1 chromium --new-window --profile-directory=Default https://web.telegram.org/ https://web.whatsapp.com/ & sleep 0.75; chromium --new-window --profile-directory=Default https://mail.google.com/mail/u/0/ https://mail.google.com/mail/u/1/ https://calendar.google.com/calendar/ & sleep 0.75; chromium --new-window --profile-directory=Default https://keep.google.com/u/0/ https://getpocket.com/a/queue/list/
 # set $fill_2 nautilus -w & nautilus -w Downloads & emacs ~/memo & chromium --new-window --profile-directory=Default https://github.com/Kappanneo https://gitlab.com/kappanneo & gnome-terminal
set $fill_2 nautilus -w & nautilus -w Downloads & emacs ~/memo & chromium --new-window --profile-directory=Default https://observablehq.com/@kappanneo & gnome-terminal

 # # # # # # # # # # # # # # # # # MODES # # # # # # # # # # # # # # # # # # # # #
#begin python

MODES = {
"$pow": # to disable standard poweroff: in /etc/systemd/logind.conf set HandlePowerKey=ignore
    ('"POWER: [q]uit  [r]estart  [s]uspend  [e]xit  [esc]"',
     "$no_border mode $pow",
     "$exec $alert $pow; fullscreen disable",
     ""),
"$wrt":
    ('"WRITE: writing enabled  [super] select container  [super+space] hover mode"',
     "$no_border mode $def",
     "$exec $alert $wrt & $touchpad_off",
     ""),
"$hov":
    ('"HOVER: writing disabled  [oklò] move cursor  [0] insert  [space|esc] exit mode"',
     "$no_border mode $hov",
     "$exec $alert $how & $touchpad_on & $enable_hover_mode",
     "$disable_hover_mode"),
"$sup":
    ('"SUPER: [wasd|oklò] select  [shift] move  [123] workspace  [space|esc] exit mode"',
     "$border mode $sup",
     "$exec $alert $sup",
     "")
}

SUBMODES = {
"$str":
    ('"START: [1|2] layouts  [space|esc] exit mode"',
     "$no_border mode $str",
     "exec $alert $str",
     ""),
"$red":
    ('"REDSH: [123] shift red level  [+] increase  [space|esc] exit mode"',
     "$no_border mode $red",
     "exec $alert $red",
     ""),
"$cnf":
    ('"CONFG: [c]onfigure i3  .git[i]gnore  [a]pplications  [e]macs  [s]tatusbar  [z]sh  [g]uide  [1|2|l]ayouts  [y]aourt  [r]edshift  [space|esc] exit mode"',
     "$no_border mode $cnf",
     "exec $alert $cnf",
     "")
}

CURRENT_MODE = "$wrt"

ALLMODES = merge(MODES,SUBMODES)

#end python

set $def "default"
<[SET(MODES)]>
 # # # # # # # # # # # # # # # # SUB-MODES # # # # # # # # # # # # # # # # # # #

<[SET(SUBMODES)]>
 # # # # # # # # # # # # # # # ON-NEW-WINDOW # # # # # # # # # # # # # # # # # #

for_window [class="."] floating disable split toggle; mode $def $no_border; fullscreen disable; $exec $disable_hover_mode & $alert $wrt

 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
 #                               COMMANDS                                      #
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

#begin python
TOP_COMMANDS={

"touchpad toggle":
    ("XF86TouchpadToggle","$exec $touchpad_toggle"),

"screen brightness controls":[
    ("XF86MonBrightnessUp","$exec $brightness_up"),
    ("XF86MonBrightnessDown","$exec $brightness_down")
],

"screenshot":
    ("--release Print","$exec $stamp"),

"display": #TODO
    ("XF86Display", "$exec xrandr --output eDP1 --mode 1920x1080 --preferred")

}

#end python
<[BINDALL(TOP_COMMANDS,"","","","$wrt")]>
 # # # # # # # # # # # # # # # MOD1-COMMANDS # # # # # # # # # # # # # # # # # #

#begin python
ALT_COMMANDS={

"kill":
    ("F4","kill"),

"browse workspaces":[
    ("Tab","workspace next"),
    ("Shift+Tab","workspace prev")
]

}

#end python
<[BINDALL(ALT_COMMANDS,"Mod1","$refresh_status_bar","","$wrt")]>
 # # # # # # # # # # # # # # # MOD4-COMMANDS # # # # # # # # # # # # # # # # # #

#begin python

SUPER_COMMANDS = {

"open terminal":
    ("Return","$exec gnome-terminal"),

"open emacs":
    ("e","exec emacs"),

"start dmenu for applications":[
    ("Menu","$exec $dmenu"),
    ("Shift+exclam","$exec $dmenu")
],

"fullscreen":[
    ("f","fullscreen toggle"),
    ("Shift+f",'$exec "sleep 0.5; xdotool key F11; i3-msg fullscreen disable"')
],

"split":[
    ("v","split v"),
    ("h","split h"),
    ("g","split v; focus parent; layout toggle split; focus child"),
],
    
"focus group":[
    ("less","focus child"),
    ("Shift+greater","focus parent")
],

"resize window":[
    ("m","resize shrink height 5 px or 1 ppt"),
    ("p","resize  grow  height 5 px or 1 ppt"),
    ("Shift+m","resize shrink width  5 px or 1 ppt"),
    ("Shift+p","resize  grow  width  5 px or 1 ppt")
]

}

SUPER_CONTROL_COMMANDS = {

"focus all":
    ("a","$focus_all"),

"kill":
    ("w","kill"),

"reload configuration":
    ("r","$no_border restart"),

"start dmenu for commands":
    ("e","$exec dmenu_run"),

"files":[
    ("f","$exec $fm"),
    ("j","$exec $fm Downloads")
],

"resize (scale)":[
    ("minus","resize shrink height 5 px or 1 ppt; resize shrink width  5 px or 1 ppt"),
    ("plus","resize  grow  height 5 px or 1 ppt; resize  grow  width  5 px or 1 ppt")
],

"save layout":
    ("s",'exec "i3-save-tree > ~/.workspaces/stamp.json; emacs ~/.workspaces/stamp.json"'),

"files":[
    ("f","$exec $fm"),
    ("j","$exec $fm Downloads")
]
    
}

ARROWS = {
"arrows":["Up","Left","Down","Right"],
"oklò":["o","k","l","ograve"],
"wasd":["w","a","s","d"]
}

DIRECTIONS = ["up","left","down","right"]

SUPER_COMMANDS_RSB = {}

K = ARROWS.keys()
K.sort()
for i in K:
    I = ARROWS[i]
    SUPER_COMMANDS_RSB[i+" focus"] = []
    SUPER_COMMANDS[i+" move"] = []
    for j in range(4):
        SUPER_COMMANDS_RSB[i+" focus"].append((I[j],"focus "+DIRECTIONS[j]))
        SUPER_COMMANDS[i+" move"].append(("Shift+"+I[j],"move "+DIRECTIONS[j]))

SUPER_COMMANDS_RSB["switch workspace"] = []

K = ALLWORKSPACES.keys()
K.sort()
for i in K:
    x,y = ALLWORKSPACES[i]
    SUPER_COMMANDS_RSB["switch workspace"].append(
        (y,"workspace {}".format(i))
    )
    
SUPER_CONTROL_COMMANDS["move focused container to workspace and follow"] = []

K = WORKSPACES.keys()
K.sort()
for i in K:
    x,y = WORKSPACES[i]
    SUPER_CONTROL_COMMANDS["move focused container to workspace and follow"].append(
        (y,"move container to workspace {}; workspace {}".format(i,i))
    )

SUPER_CONTROL_COMMANDS_RSB = {

"kill":
    ("w","kill"),

"cut":
    ("x","move container to workspace $wx"),

"paste":
    ("v","$exec i3-msg 'workspace --no-auto-back-and-forth $wx; move container to workspace $wx; workspace $wx'")

}    

#end python
<[BINDALL(SUPER_COMMANDS,"Mod4","","","$wrt")]>
<[BINDALL(SUPER_COMMANDS_RSB,"Mod4","$refresh_status_bar","","$wrt")]>
<[BINDALL(SUPER_CONTROL_COMMANDS,"Mod4+control","","","$wrt")]>
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
 #                                  MODES                                      #
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

<[BIND_TO_MODE(("XF86PowerOff",""),"$wrt","$pow")]>
<[BIND_TO_MODE(("--release Super_L",""),"$wrt","$sup")]>
<[BIND_TO_MODE(("Mod4+space",""),"$wrt","$sup")]>
<[BIND_TO_MODE(("Mod4+r",""),"$wrt","$red")]>
<[BIND_TO_MODE(("Mod4+z",""),"$wrt","$str")]>
<[BIND_TO_MODE(("Mod4+c",""),"$wrt","$cnf")]>
 # # # # # # # # # # # # # # # # #SUPER-MODE # # # # # # # # # # # # # # # # # #

<[BEGIN_MODE("$sup")]>

 # # # # # # # MODES # # # # # # #

<[BIND_TO_MODE(("XF86PowerOff",""),"$sup","$pow")]>
<[BINDALL_TO_MODE({"exit to write mode":[
    ("Escape",""),
    ("Super_L",""),
    ("'Alt_L'",""),
    ("space",""),
    ("Delete",""),
    ("BackSpace",""),
    ("Return",""),
    ("Tab",""),
    ("$alt_gr",""),
    ("control+e","$exec dmenu_run"),
    ("Menu","$exec $dmenu"),
    ("--border button2","")
]},"$sup","$wrt")]>
<[BIND_TO_MODE(("r",""),"$sup","$red")]>
<[BIND_TO_MODE(("z",""),"$sup","$str")]>
<[BIND_TO_MODE(("c",""),"$sup","$cnf")]>

 # # # # # # COMMANDS # # # # # #

<[BINDALL(TOP_COMMANDS,"","","","$sup")]>
<[BINDALL(ALT_COMMANDS,"Mod1","","","$sup")]>
<[BINDALL(SUPER_COMMANDS,"","","","$sup")]>
<[BINDALL(SUPER_COMMANDS_RSB,"","$refresh_status_bar","","$sup")]>
<[BINDALL(SUPER_CONTROL_COMMANDS,"control","","","$sup")]>
<[BINDALL(SUPER_CONTROL_COMMANDS_RSB,"control","$refresh_status_bar","","$sup")]>
         
<[END_MODE("$sup")]>

 # # # # # # # # # # # # # # # # HOVER-MODE # # # # # # # # # # # # # # # # # # #

<[BEGIN_MODE("$hov")]>

 # # # # # # # # MODES # # # # # # #

<[BIND_TO_MODE(("XF86PowerOff",""),"$hov","$pow")]>
<[BINDALL_TO_MODE({"exit to write mode":[
    ("Escape",""),
    ("Delete",""),
    ("BackSpace",""),
    ("Mod4+control+e","$exec dmenu_run"),
    ("Mod4+Menu","$exec $dmenu"),
    ("--border button2","")
]},"$hov","$wrt")]>
<[BIND_TO_MODE(("Mod4+r",""),"$hov","$red")]>
<[BIND_TO_MODE(("Mod4+z",""),"$hov","$str")]>
<[BIND_TO_MODE(("Mod4+c",""),"$hov","$cnf")]>

 # # # # # # # COMMANDS # # # # # #

<[BINDALL(TOP_COMMANDS,"","","","$hov")]>
<[BINDALL(ALT_COMMANDS,"Mod1","","","$hov")]>
<[BINDALL(SUPER_COMMANDS,"Mod4","","","$hov")]>
<[BINDALL(SUPER_COMMANDS_RSB,"Mod4","$refresh_status_bar","","$hov")]>
<[BINDALL(SUPER_CONTROL_COMMANDS,"Mod4+control","","","$hov")]>
<[BINDALL(SUPER_CONTROL_COMMANDS_RSB,"Mod4+control","$refresh_status_bar","","$hov")]>
 
 # # # # # # UNUSED KEYS # # # # # #

<[END_MODE("$hov")]>
 
 # # # # # # # # # # # # # # # POWEROFF-MODE # # # # # # # # # # # # # # # # # #

<[BEGIN_MODE("$pow")]>
<[BINDALL({"options":[
    ("XF86PowerOff","$exec $alert $pow"),
    ("q","$exec poweroff"),
    ("r","$exec reboot"),
    ("e","$exec exit")
]},"","","","$pow")]>
<[BIND_TO_MODE(('"Super_L"',""),"$pow","$sup")]>
<[BINDALL_TO_MODE({"exit to write mode":[
    ("Escape",""),
    ("'Alt_L'",""),
    ("space",""),
    ("Delete",""),
    ("BackSpace",""),
    ("Return",""),
    ("Tab",""),
    ("$alt_gr",""),
    ("--border button2",""),
    ("s","mode $def $exec systemctl suspend")
]},"$pow","$wrt")]>
<[END_MODE("$pow")]>

 # # # # # # # # # # # # # # # # SUB-MODES # # # # # # # # # # # # # # # # # # # #
#begin python

def MAKE_SUBMODE(mode_tag,OPTIONS):
    string = ""
    string += BEGIN_MODE(mode_tag)
    string += OPTIONS
    string += BIND_TO_MODE(("XF86PowerOff",""),"$red","$pow")
    string += BIND_TO_MODE(('"Super_L"',""),"$red","$sup")
    string += BINDALL_TO_MODE({"exit to write mode":[
        ("Escape",""),
        ("'Alt_L'",""),
        ("space",""),
        ("Delete",""),
        ("BackSpace",""),
        ("Return",""),
        ("Tab",""),
        ("$alt_gr",""),
        ("--border button2","")
    ]},"$red","$wrt")
    string += BINDALL_TO_MODE(TOP_COMMANDS,"$red","$wrt")
    string += END_MODE("$red")
    return string

#end python
 
 # redshift
<[MAKE_SUBMODE("$red",BINDALL({"options":[    
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
]},"","","","$red"))]>

 # start layout
<[MAKE_SUBMODE("$str",BINDALL_TO_MODE({"options":[    
    ("1",'$exec "$layout_1; $fill_1"'),
    ("2",'$exec "$layout_2; $fill_2"'),
]},"$str","$wrt"))]>

 # configuration files launcher
<[MAKE_SUBMODE("$cnf",BINDALL_TO_MODE({"options":[    
    ("c","$exec emacs ~/.i3/config.py"),                                  
    ("i","$exec emacs ~/.gitignore"),
    ("a","$exec emacs /sudo::/usr/share/applications/"),
    ("e","$exec emacs ~/.emacs"),
    ("s","$exec emacs ~/.config/i3status/config"),
    ("z","$exec emacs ~/.zshrc"),
    ("g","$exec chromium --new-window i3wm.org/docs/userguide.html"),
    ("l","$exec emacs ~/.workspaces/stamp.json"),
    ("1","$exec emacs ~/.workspaces/$w1.json"),
    ("2","$exec emacs ~/.workspaces/$w2.json"),
    ("y","$exec emacs /sudo::/etc/yaourtrc"),
    ("r","$exec emacs ~/.config/redshift/redshift.conf")
]},"$cnf","$wrt"))]>

 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
 #                              STATUS-BAR                                     #
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

 # Start i3bar to display a workspace bar (plus the system information i3status finds out, if available)
bar {
        status_command    ./.bin/my_status.sh
        position          bottom
        mode              dock
        workspace_buttons yes
        colors {
                   background #000000
                   statusline #999999
                   focused_workspace  #ffffff #000000
                   active_workspace   #ffffff #000000
                   inactive_workspace #888888 #000000
                   urgent_workspace   #ffffff #000000
               }

        # disable scrolling on status bar
 #       bindsym button4 nop # scroll wheel up
 #       bindsym button5 nop # scroll wheel down
        # mid-mouse click to lock
 #       bindsym button2 mode $def $no_border $exec $alert $wrt & $touchpad_off_2 & $disable_hover_mode
    }

 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
 #                              APPLICATIONS                                   #
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

 # code
assign [class=".*code.*"] $w3

 # android studio
assign [class="jetbrains-studio"] $w3

 # steam
assign [class="Steam"] $w5
assign [class="Wine"] $w5
for_window [title="Steam - News"] kill
for_window [title="Friends"] resize shrink width 22 px or 22 ppt; split h
for_window [title="Steam"] split h

 # discord and skype
assign [class="discord"] $w6
assign [title=".*skype.*"] $w6

 # texmaker
assign [title="Texmaker"] $w7
assign [title=".*overleaf.*"] $w7

 # gimp
assign [class="Gimp.*"] $w9

 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
 #                                STARTUP                                      #
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

 # keybinding (order matters)
$exec $disable_Caps

 # autoscroll (not always permanent, may need reaload)
$exec_always $enable_autoscroll

 # background (not always permanent)
$exec_always nitrogen --restore

 # bar applications
$exec nm-applet
$exec pamac-tray
$exec pa-applet
$exec clipit

 # background applications
$exec /usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1

 # reshift oneshot mode (to set starting temperature according to time)
$exec redshift -o

 # layout
$exec $layout_2; $fill_2

 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
 #                                  FIN                                        #
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
