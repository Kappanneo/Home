#include "forall.py"
#include "arrows.py"
#include "workspaces.py"
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
    ("--release Print","$exec i3-scrot"),
    
"display": #TODO
    ("XF86Display", "$exec xrandr --output eDP1 --mode 1920x1080 --preferred"),

"borders":
    ("--border button2","$no_border"),

}

TOP_COMMANDS_TO_WRITE = {

"no border write":
    ('Shift+"Super_L"',"$no_border"),

}

TOP_COMMANDS_TO_HOVER = {

"where am i?":
    ('--release "Super_L"',"$border, $focus_one, fullscreen disable; $exec $touchpad_off"),

"no border hover":
    ('Shift+Menu',"$no_border"),
}

ALT_COMMANDS_RSB={

"kill":
    ("F4","kill"),

}

SUPER_COMMANDS = {

"open terminal":
    ("Return","exec gnome-terminal"),

"open emacs":
    ("e","exec $emacs"),

"fullscreen":[
    ("f","fullscreen toggle"),
    ("Shift+f",'$exec "sleep 0.5; xdotool key F11; i3-msg fullscreen disable"')
],

"split orientation":[
    ("v","split v; exec notify-send 'vertical'"),
    ("h","split h; exec notify-send 'horizontal'"),
    ("g","split v; focus parent; layout toggle split; focus child"),
],

"borders":[
    ("b","$border"),
    ("Shift+b","$no_border")
],

"focus group":[
    ("less","focus child"),
    ("Shift+greater","focus parent")
],

"resize window":[
    ("i","resize shrink height 5 px or 5 ppt"),
    ("p","resize  grow  height 5 px or 5 ppt"),
    ("Prior","resize shrink height 5 px or 5 ppt"),
    ("Next", "resize  grow  height 5 px or 5 ppt"),
    ("Shift+i","resize shrink width  5 px or 5 ppt"),
    ("Shift+p","resize  grow  width  5 px or 5 ppt"),
    ("Shift+Prior","resize shrink width  5 px or 5 ppt"),
    ("Shift+Next", "resize  grow  width  5 px or 5 ppt"),
],

"browse workspaces":[
    ("j","workspace prev"),
    ("agrave","workspace next"),
    ("ugrave","workspace back_and_forth")
]}

SUPER_CONTROL_COMMANDS = {

"focus all":
    ("a","$focus_all"),

"reload configuration":[
    ("r",'$exec "make -C ~/.i3 && i3-msg $no_border restart"'),
    ("Shift+r", '$exec "make -C ~/.i3 stable && i3-msg $no_border restart"')
],

"files":[
    ("f","exec $fm"),
    ("j","exec $fm Downloads")
],

"save layout":
    ("s",'exec "i3-save-tree > ~/.workspaces/stamp.json; $emacs ~/.workspaces/stamp.json"'),

"files":[
    ("f","$exec $fm"),
    ("j","$exec $fm Downloads")
],
  
"resize (precise)":[
    ("i","resize shrink height 1 px or 1 ppt"),
    ("p","resize  grow  height 1 px or 1 ppt"),
    ("Prior","resize shrink height 1 px or 1 ppt"),
    ("Next", "resize  grow  height 1 px or 1 ppt"),
    ("Shift+i","resize shrink width  1 px or 1 ppt"),
    ("Shift+p","resize  grow  width  1 px or 1 ppt"),
    ("Shift+Prior","resize shrink width  1 px or 1 ppt"),
    ("Shift+Next", "resize  grow  width  1 px or 1 ppt"),
],
    
"resize (scale)":[
    ("minus","resize shrink height 5 px or 5 ppt; resize shrink width  5 px or 5 ppt"),
    ("plus","resize  grow  height 5 px or 5 ppt; resize  grow  width  5 px or 5 ppt"),
    ("Shift+minus","resize shrink height 1 px or 1 ppt; resize shrink width  1 px or 1 ppt"),
    ("Shift+plus","resize  grow  height 1 px or 1 ppt; resize  grow  width  1 px or 1 ppt"),
]}

SUPER_COMMANDS_TO_HOVER_RSB = {

"browse workspaces":[
    ("Tab","workspace next"),
    ("Shift+Tab","workspace prev")
]

}
    
SUPER_CONTROL_COMMANDS["move focused container to workspace and follow"] = []

def move_to_workspace(d,i):
    _, key = d
    SUPER_CONTROL_COMMANDS["move focused container to workspace and follow"].append(
        (key,"move container to workspace {}; workspace {}".format(i,i))
    )

forall(WORKSPACES, move_to_workspace)

SUPER_CONTROL_COMMANDS_TO_HOVER_RSB = {

"kill":
    ("w","kill"),

"cut":
    ("x","move container to workspace $wx"),

"paste":
    ("v","$exec i3-msg 'workspace --no-auto-back-and-forth $wx; move container to workspace $wx; workspace $wx;'")
}

DIRECTIONS = ["up","left","down","right"]

def move_and_focus(d,i):
    SUPER_COMMANDS[i+" move"] = []
    SUPER_COMMANDS_TO_HOVER_RSB[i+" focus"] = []
    for j in range(len(d)):
        SUPER_COMMANDS[i+" move"].append(("Shift+"+d[j],"move "+DIRECTIONS[j]))
        SUPER_COMMANDS_TO_HOVER_RSB[i+" focus"].append((d[j],"focus "+DIRECTIONS[j]))

forall(ARROWS,move_and_focus)

SUPER_COMMANDS_TO_HOVER_RSB["switch workspace"] = []

def switch_workspace(d,i):
    _, key = d
    SUPER_COMMANDS_TO_HOVER_RSB["switch workspace"].append(
        (key,"workspace {}".format(i))
    )

forall(WORKSPACES,switch_workspace)

SUPER_COMMANDS_TO_WRITE = {

"start dmenu for applications":
    ("Shift+exclam","$exec $dmenu"),

"start dmenu for commands":
    ("control+e","$exec dmenu_run"),

}

SUPER_COMMANDS_TO_HOVER = {

"application menu":
    ("Menu","exec morc_menu"),

}

#end python
