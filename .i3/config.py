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
        string += " set {} {}\n".format(x,t[0])
    return string

def BIND((x,y),current_mode=None,after_mode=None,modifier="",prefix="",postfix=""):
    if postfix != "" and y != "": y += "; " + postfix
    if postfix != "" and y == "": y += postfix
    if prefix != "" and y != "": y = prefix + " " + y
    if prefix != "" and y == "": y = prefix
    if modifier != "": x = modifier + "+" + x
    if current_mode:
        USED_KEYS[current_mode].append(x)
        #if "Shift" in x and not any([x for x in ['"Shift_L"','"Shift_R"'] if x in USED]):
        #    USED_KEYS[current_mode].extend(['"Shift_L"','"Shift_R"'])
        #if "control" in x and not any([x for x in ['"Control_L"','"Control_R"'] if x in USED]):
        #    USED_KEYS[current_mode].extend(['"Control_L"','"Control_R"'])
    if after_mode:
        name, pre, post, _ = ALLMODES[after_mode]
        if post != "" and y != "": y += "; " + post
        if post != "" and y == "": y += post
        if pre != "" and y != "": y = pre + " " + y
        if pre != "" and y == "": y = pre
        if current_mode:
            _, _, _, exit = ALLMODES[current_mode]
            if exit != "": y += "; " + exit
    return " bindsym {} {}\n".format(x,y)

def BINDBLOCKS(blocks,current_mode=None,after_mode=None,modifier="",prefix="",postfix=""):
    string = ""
    K = blocks.keys()
    K.sort()
    for name in K:
        string += " # {}\n".format(name)
        x = blocks[name]
        if type(x) == tuple:
            string += BIND(x,current_mode,after_mode,modifier,prefix,postfix)
        elif type(x) == list:
            for t in x:
                string += BIND(t,current_mode,after_mode,modifier,prefix,postfix)
        string += "\n"
    return string

def LOCK(mode,free_keys=[]):
    F = USED_KEYS[mode] + free_keys 
    string = "";
    U = [(x,"nop") for x in KEYS if x not in F]
    string += BINDBLOCKS({"unused keys":U})
    return string

def LOCK_SHIFT(mode,free_keys=[]):
    F = USED_KEYS[mode] + ['Shift'+y for y in free_keys] 
    string = "";
    U = [(x,"nop") for x in ['Shift+'+y for y in SHIFT_KEYS] if x not in F]
    string += BINDBLOCKS({"also Shift+ (since Shift is not locked)":U})
    return string

def LOCK_CONTROL(mode,free_keys=[]):
    F = USED_KEYS[mode] + ['control'+y for y in free_keys] 
    string = "";
    U = [(x,"nop") for x in ['control+'+y for y in KEYS if y not in ['"Control_L"','"Control_R"']] if x not in F]
    string += BINDBLOCKS({"also control+ (since control is not locked)":U})
    return string    

def MAKE_SUBMODE(options,mode_tag,after_mode=None,free_keys=[]):
    string = " mode "+mode_tag+" {\n"
    string += BINDBLOCKS({"options":options},mode_tag,after_mode)
    string += BIND(("XF86PowerOff",""),mode_tag,"$pow")
    string += BIND(('"Super_L"',""),mode_tag,"$sup")
    string += BINDBLOCKS({"exit to write mode":[(x,"") for x in DEFAULT_EXIT_KEYS]},mode_tag,"$wrt")
    string += BINDBLOCKS(TOP_COMMANDS,mode_tag,"$wrt")
    string += LOCK(mode_tag,free_keys=[])
    string += " }"
    return string

USED_KEYS ={}

DEFAULT_EXIT_KEYS = [
"space",           
"Delete",          
"BackSpace",       
"Return",          
"Tab",             
"$alt_gr",
'"Alt_L"',
"--border button2",
"control+z",
]

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
'apostrophe',
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
'"Caps_Lock"',
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

#end python
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
 #                               SETTINGS                                      #
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

 # i3 config file (v4)
 # Please see http://i3wm.org/docs/userguide.html for a complete reference!
 
 # Set mod key (Mod1=<Alt>, Mod4=<Super>)
 set $mod Mod4
 
 # set default desktop layout (default is tiling)
 # workspace_layout tabbed <stacking|tabbed>
 
 # Configure border style <normal|1pixel|pixel xx|none|pixel>
 new_window pixel 0
 new_float normal
 
 # Hide borders
 hide_edge_borders none
 
 # Font for window titles. Will also be used by the bar unless a different font
 # is used in the bar {} block below.
 font pango:DejaVu Sans Mono 8

 # go back to previous workspace if you try to go to the current one
 # (allow for fast window movement to a workspace and back)
 workspace_auto_back_and_forth yes

 # focus on mouseover (is a pain if you happen to have a mouse)
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
 set $enable_Caps setxkbmap -option
 set $disable_hover_mode ~/.bin/hover.sh 0
 set $enable_hover_mode ~/.bin/hover.sh 1

 # # # # # # # # # # # # # # # FUNCTIONALITIES # # # # # # # # # # # # # # # # #

 # touchpad toggle
 set $touchpad_on ~/.bin/touchpad_toggle.sh 1 & xdotool mousemove  750  350
 set $touchpad_off ~/.bin/touchpad_toggle.sh 0 & xdotool mousemove 2500 1200
 set $touchpad_off_2 ~/.bin/touchpad_toggle.sh 0
 set $touchpad_toggle ~/.bin/touchpad_toggle.sh

 # autoscroll
 set $disable_autoscroll ~/.bin/autoscroll.sh 0
 set $enable_autoscroll ~/.bin/autoscroll.sh 1

 # screenshot (-w -> window, -s -> mouse selection)
 set $stamp exec --no-startup-id i3-scrot
 
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
    ('"POWER: [q]uit  [r]estart  [s]uspend  [h]ibernate  [esc]"',
     "$no_border mode $pow",
     "$exec $alert $pow, fullscreen disable",
     ""),

"$wrt":
    ('"WRITE: writing enabled"',
     "$no_border mode $def",
     "$exec $alert $wrt",
     ""),

"$tch":
    ('"TOUCH: touchpad enabled  [space|esc] write mode"',
     "$no_border mode $tch",
     "$exec $alert $tch & $touchpad_on",
     "$exec $touchpad_off"),

"$sup":
    ('"SUPER: [oklò] select  [shift+] move  [123] workspace  [Menu] hover mode  [super+space] touch mode  [space|esc] write mode"',
     "$border mode $sup",
     "$exec $alert $sup, $focus_one fullscreen disable",
     ""),

"$hov":
    ('"HOVER: writing disabled  [oklò] move cursor  [0] insert  [space|esc] write mode"',
     "$no_border mode $hov",
     "$exec $alert $hov & $enable_hover_mode",
     "$exec $disable_hover_mode"),
} 

SUBMODES = {

"$str":
    ('"START: [1|2] layouts  [space|esc] exit mode"',
     "$no_border mode $str",
     "$exec $alert $str",
     ""),

"$red":
    ('"REDSH: [123] shift red level  [+] increase  [space|esc] exit mode"',
     "$no_border mode $red",
     "$exec $alert $red",
     ""),

"$cnf":
    ('"CONFG: [c]onfigure i3  .git[i]gnore  [a]pplications  [e]macs  [s]tatusbar  [z]sh  [g]uide  [1|2|l]ayouts  [r]edshift  [space|esc] exit mode"',
     "$no_border mode $cnf",
     "$exec $alert $cnf",
     ""),
}

ALLMODES = merge(MODES,SUBMODES)
for x in ALLMODES.keys():
    USED_KEYS[x] = []

#end python

 set $def "default"
<[SET(MODES)]>

 # # # # # # # # # # # # # # # # SUB-MODES # # # # # # # # # # # # # # # # # # #

<[SET(SUBMODES)]>

 # # # # # # # # # # # # # # # ON-NEW-WINDOW # # # # # # # # # # # # # # # # # #

 for_window [class=".?" title=".?"] floating disable split toggle; mode $hov $no_border; fullscreen disable; $exec $enable_hover_mode & $touchpad_disable $alert $hov

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

"screen poweroff":
    ("XF86ScreenSaver","$exec xset dpms force off"),

"screenshot":
    ("--release Print","$exec $stamp"),
    
"display": #TODO
    ("XF86Display", "$exec xrandr --output eDP1 --mode 1920x1080 --preferred")

}
#end python

<[BINDBLOCKS(TOP_COMMANDS,"$wrt")]>

 # # # # # # # # # # # # # # # MOD1-COMMANDS # # # # # # # # # # # # # # # # # #
#begin python

ALT_COMMANDS_RSB={

"kill":
    ("F4","kill"),

"browse workspaces":[
    ("Tab","workspace next"),
    ("Shift+Tab","workspace prev")
]

}
#end python

<[BINDBLOCKS(ALT_COMMANDS_RSB,"$wrt","$hov",modifier="Mod1",postfix="$refresh_status_bar")]>

 # # # # # # # # # # # # # # # MOD4-COMMANDS # # # # # # # # # # # # # # # # # #
#begin python
SUPER_COMMANDS = {

"open terminal":
    ("Return","exec gnome-terminal"),

"open emacs":
    ("e","exec emacs"),

"fullscreen":[
    ("f","fullscreen toggle"),
    ("Shift+f",'$exec "sleep 0.5; xdotool key F11; i3-msg fullscreen disable"')
],

"split orientation":[
    ("v","split v; exec notify-send 'vertical'"),
    ("h","split h; exec notify-send 'horizontal'"),
    ("g","split v; focus parent; layout toggle split; focus child"),
],
    
"focus group":[
    ("less","focus child"),
    ("Shift+greater","focus parent")
],

"resize window":[
    ("i","resize shrink height 5 px or 5 ppt"),
    ("p","resize  grow  height 5 px or 5 ppt"),
    ("Shift+i","resize shrink width  5 px or 5 ppt"),
    ("Shift+p","resize  grow  width  5 px or 5 ppt"),
],

"browse workspaces":[
    ("j","workspace prev"),
    ("agrave","workspace next"),
    ("ugrave","workspace back_and_forth")
]}

SUPER_CONTROL_COMMANDS = {

"focus all":
    ("a","$focus_all"),

"reload configuration":
    ("r","$no_border restart"),

"files":[
    ("f","exec $fm"),
    ("j","exec $fm Downloads")
],

"save layout":
    ("s",'exec "i3-save-tree > ~/.workspaces/stamp.json; emacs ~/.workspaces/stamp.json"'),

"files":[
    ("f","$exec $fm"),
    ("j","$exec $fm Downloads")
],
  
"resize (precise)":[
    ("i","resize shrink height 1 px or 1 ppt"),
    ("p","resize  grow  height 1 px or 1 ppt"),
    ("Shift+i","resize shrink width  1 px or 1 ppt"),
    ("Shift+p","resize  grow  width  1 px or 1 ppt"),
],
    
"resize (scale)":[
    ("minus","resize shrink height 5 px or 5 ppt; resize shrink width  5 px or 5 ppt"),
    ("plus","resize  grow  height 5 px or 5 ppt; resize  grow  width  5 px or 5 ppt"),
    ("Shift+minus","resize shrink height 1 px or 1 ppt; resize shrink width  1 px or 1 ppt"),
    ("Shift+plus","resize  grow  height 1 px or 1 ppt; resize  grow  width  1 px or 1 ppt"),
]}

SUPER_COMMANDS_RSB = {}
    
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

ARROWS = {
"default":["Up","Left","Down","Right"],
"oklò":["o","k","l","ograve"],
"wasd":["w","a","s","d"]
}

DIRECTIONS = ["up","left","down","right"]

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

DMENU_COMMANDS = {

"start dmenu for applications":
    ("Shift+exclam","$exec $dmenu"),

"start dmenu for commands":
    ("control+e","$exec dmenu_run"),

}
#end python

<[BINDBLOCKS(DMENU_COMMANDS,"$wrt",modifier="Mod4")]>
<[BINDBLOCKS(SUPER_COMMANDS,"$wrt",modifier="Mod4")]>
<[BINDBLOCKS(SUPER_COMMANDS_RSB,"$wrt","$hov",modifier="Mod4",postfix="$refresh_status_bar")]>
<[BINDBLOCKS(SUPER_CONTROL_COMMANDS,"$wrt",modifier="Mod4+control")]>
<[BINDBLOCKS(SUPER_CONTROL_COMMANDS_RSB,"$wrt","$hov",modifier="Mod4+control",postfix="$refresh_status_bar")]>

 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
 #                                  MODES                                      #
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

<[BIND(("XF86PowerOff",""),"$wrt","$pow")]>
<[BIND(('--release "Super_L"',""),"$wrt","$sup")]>
<[BIND(("Menu",""),"$wrt","$hov")]>
<[BIND(("Mod4+Menu",""),"$wrt","$hov")]>
<[BIND(("Mod4+space",""),"$wrt","$tch")]>
<[BIND(("Mod4+r",""),"$wrt","$red")]>
<[BIND(("Mod4+z",""),"$wrt","$str")]>
<[BIND(("Mod4+c",""),"$wrt","$cnf")]>

 # # # # # # # # # # # # # # # POWEROFF-MODE # # # # # # # # # # # # # # # # # #

 mode $pow {
<[BINDBLOCKS({"options":[
    ("XF86PowerOff","$exec $alert $pow"),
    ("q","$exec systemctl poweroff"),
    ("r","$exec systemctl reboot"),
    ("s","$exec systemctl suspend"),
    ("h","$exec systemctl hibernate")
]},"$pow","$wrt")]>
<[BINDBLOCKS({"exit to write mode":[(x,"") for x in DEFAULT_EXIT_KEYS]},"$pow","$wrt")]>
<[BIND(('"Super_L"',""),"$pow","$sup")]>
<[BIND(('Menu',""),"$pow","$hov")]>
<[LOCK("$pow")]>
 }

 # # # # # # # # # # # # # # # # #TOUCH-MODE # # # # # # # # # # # # # # # # # #

 mode $tch {
 # # # # # # # MODES # # # # # # #

<[BIND(("XF86PowerOff",""),"$tch","$pow")]>
<[BINDBLOCKS({"exit to write mode":[(x,"") for x in DEFAULT_EXIT_KEYS]},"$tch","$wrt")]>
<[BIND(('--release "Super_L"',""),"$tch","$sup")]>
<[BIND(("Menu",""),"$tch","$hov")]>
<[LOCK("$tch")]>     

<[BINDBLOCKS(DMENU_COMMANDS,"$tch","$wrt",modifier="Mod4")]>
<[BINDBLOCKS(SUPER_COMMANDS,"$tch",modifier="Mod4")]>
<[BINDBLOCKS(SUPER_COMMANDS_RSB,"$tch","$hov",modifier="Mod4",postfix="$refresh_status_bar")]>
<[BINDBLOCKS(SUPER_CONTROL_COMMANDS,"$tch",modifier="Mod4+control")]>
<[BINDBLOCKS(SUPER_CONTROL_COMMANDS_RSB,"$tch","$hov",modifier="Mod4+control",postfix="$refresh_status_bar")]>

 }
 
 # # # # # # # # # # # # # # # # #SUPER-MODE # # # # # # # # # # # # # # # # # #

 mode $sup {
 
 # # # # # # # MODES # # # # # # #

<[BIND(("XF86PowerOff",""),"$sup","$pow")]>
<[BINDBLOCKS({"exit to write mode":[(x,"") for x in DEFAULT_EXIT_KEYS]},"$sup","$wrt")]>
<[BIND(("Menu",""),"$sup","$hov")]>
<[BIND(("r",""),"$sup","$red")]>
<[BIND(("z",""),"$sup","$str")]>
<[BIND(("c",""),"$sup","$cnf")]>
<[BIND(("Mod4+r",""),"$sup","$red")]>
<[BIND(("Mod4+z",""),"$sup","$str")]>
<[BIND(("Mod4+c",""),"$sup","$cnf")]>
<[BIND(("Mod4+space",""),"$sup","$tch")]>     
<[BIND(("Mod4+Menu",""),"$sup","$hov")]>

 # # # # # # COMMANDS # # # # # #

<[BIND(('"Super_L"',"fullscreen disable $exec $focus_one"),"$sup")]>

<[BINDBLOCKS(TOP_COMMANDS,"$sup","$hov")]>

<[BINDBLOCKS(DMENU_COMMANDS,"$sup","$wrt")]>
<[BINDBLOCKS(SUPER_COMMANDS,"$sup")]>
<[BINDBLOCKS(SUPER_COMMANDS_RSB,"$sup",postfix="$refresh_status_bar")]>
<[BINDBLOCKS(SUPER_CONTROL_COMMANDS,"$sup",modifier="control")]>
<[BINDBLOCKS(SUPER_CONTROL_COMMANDS_RSB,"$sup",modifier="control",postfix="$refresh_status_bar")]>

 # # # # # MOD4-COMMANDS # # # # #

<[BINDBLOCKS(DMENU_COMMANDS,"$sup","$wrt",modifier="Mod4")]>
<[BINDBLOCKS(SUPER_COMMANDS,"$sup","$hov",modifier="Mod4")]>
<[BINDBLOCKS(SUPER_COMMANDS_RSB,"$sup","$hov",modifier="Mod4",postfix="$refresh_status_bar")]>
<[BINDBLOCKS(SUPER_CONTROL_COMMANDS,"$sup","$hov",modifier="control+Mod4")]>
<[BINDBLOCKS(SUPER_CONTROL_COMMANDS_RSB,"$sup","$hov",modifier="control+Mod4",postfix="$refresh_status_bar")]>

 # # # # # # # LOCKS # # # # # # #
     
<[LOCK("$sup",ARROWS["default"])]>
<[LOCK_SHIFT("$sup")]>
<[LOCK_CONTROL("$sup",["Tab"])]>
 }

 # # # # # # # # # # # # # # # # HOVER-MODE # # # # # # # # # # # # # # # # # # #

 mode $hov {

 # # # # # # # # MODES # # # # # # #

<[BIND(("XF86PowerOff",""),"$hov","$pow")]>
<[BINDBLOCKS({"exit to write mode":[(x,"") for x in DEFAULT_EXIT_KEYS if x not in ['"Alt_L"',"Return","Tab"]]},"$hov","$wrt")]>
<[BIND(('--release "Super_L"',""),"$hov","$sup")]>
<[BIND(("Mod4+r",""),"$hov","$red")]>
<[BIND(("Mod4+z",""),"$hov","$str")]>
<[BIND(("Mod4+c",""),"$hov","$cnf")]>
<[BIND(("Mod4+space",""),"$hov","$tch")]>

 # # # # # # # COMMANDS # # # # # #


<[BINDBLOCKS(TOP_COMMANDS,"$hov")]>
<[BINDBLOCKS(ALT_COMMANDS_RSB,"$hov",modifier="Mod1",postfix="$refresh_status_bar")]>
<[BINDBLOCKS(DMENU_COMMANDS,"$hov","$wrt",modifier="Mod4")]>
<[BINDBLOCKS(SUPER_COMMANDS,"$hov",modifier="Mod4")]>
<[BINDBLOCKS(SUPER_COMMANDS_RSB,"$hov",modifier="Mod4",postfix="$refresh_status_bar")]>
<[BINDBLOCKS(SUPER_CONTROL_COMMANDS,"$hov",modifier="Mod4+control")]>
<[BINDBLOCKS(SUPER_CONTROL_COMMANDS_RSB,"$hov",modifier="Mod4+control",postfix="$refresh_status_bar")]>
 
 # # # # # # UNUSED KEYS # # # # # #

<[LOCK("$hov",ARROWS["default"]+['"Alt_L"','"Control_L"','"Shift_L"',"space","Return","Tab"])]>
<[LOCK_SHIFT("$hov",ARROWS["default"])]>
 }
     
 # # # # # # # # # # # # # # # # SUB-MODES # # # # # # # # # # # # # # # # # # # #

 # redshift
<[MAKE_SUBMODE([    
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
],"$red")]>

 # start layout
<[MAKE_SUBMODE([    
    ("1",'$exec "$layout_1; $fill_1"'),
    ("2",'$exec "$layout_2; $fill_2"'),
],"$str","$wrt")]>

 # configuration files launcher
<[MAKE_SUBMODE([    
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
    ("r","$exec emacs ~/.config/redshift/redshift.conf")
],"$cnf","$wrt")]>

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
        bindsym button4 nop # scroll wheel up
        bindsym button5 nop # scroll wheel down
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
 assign [title="Skype"] $w6

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
 $exec_always fix_xcursor

 # background applications
 $exec /usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1
 $exec nitrogen --restore; sleep 1; compton -b
 $exec xfce4-power-manager
 $exec start_conky_maja

 # bar applications
 $exec nm-applet
 $exec pamac-tray
 $exec pa-applet
 $exec clipit

 # reshift oneshot mode (to set starting temperature according to time)
 $exec redshift -o

 # layout
 $exec $layout_2; $fill_2

 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
 #                                  FIN                                        #
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
 
