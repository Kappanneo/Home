#include "forall.py"
#include "arrows.py"
#include "workspaces.py"
#begin python

TOP_COMMANDS = {

"touchpad toggle":
    ("XF86TouchpadToggle","$exec $touchpad_toggle"),

"screen brightness controls":[
    ("XF86MonBrightnessUp","$brightness_up"),
    ("XF86MonBrightnessDown","$brightness_down")
],

"screen poweroff":
    ("XF86ScreenSaver","$exec xset dpms force off"),

"screenshot":[
    ("--release Print","$exec i3-scrot"),
    ("--release Mod4+Print","$exec i3-scrot -w"),
    ("--release Mod4+control+Print","$exec i3-scrot -s"),
],

"display": #TODO
    ("XF86Display", "$exec xrandr --output eDP1 --mode 1920x1080 --preferred"),

}

TOP_COMMANDS_TO_DEFLT = {

"middle mouse to default":
    ("--border button2","$no_border"),

}

TOP_COMMANDS_TO_WRITE = {

"delete to write":[
    ("Delete",''),
    ("BackSpace",''),
],

}

MOD1_COMMANDS_RSB = {

"kill":
    ("F4","kill"),

}

MOD4_COMMANDS = {

"open terminal":
    ("Return","exec gnome-terminal"),

"open emacs":[
    ("e","$exec $emacs"),
    ("Shift+e","$exec pkill emacs"),
],

"fullscreen":
    ("f","fullscreen toggle"),

"split orientation":[
    ("v","split v; exec notify-send 'vertical'"),
    ("h","split h; exec notify-send 'horizontal'"),
    ("g","split v; focus parent; layout toggle split; focus child"),
],

"borders":[
    ("x","$border $focus_one fullscreen disable"),
    ("Shift+x","$no_border $focus_one")
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

#"mouse kill":
#    ("q --release","$exec xkill"),

}

MOD4_COMMANDS_RSB = {

"browse workspaces":[
    ("Tab","workspace next"),
    ("Shift+Tab","workspace prev"),
    ("j","workspace prev"),
    ("agrave","workspace next"),
    ("Home","workspace prev"),
    ("End","workspace next"),
    ("ugrave","workspace back_and_forth"),
],

}

MOD4_COMMANDS_TO_SUPER = {

"application menu":
    ("Menu","$exec morc_menu"),

"disable_touchpad":
    ("Shift+space","$exec $touchpad_x_off"),

}

MOD4_COMMANDS_TO_TOUCH = {

"enable touchpad":
    ("space","$exec $touchpad_x_on"),

}

MOD4_COMMANDS_TO_DEFLT = {

"start dmenu for applications":
    ("Shift+exclam","$exec $dmenu"),

"start dmenu for commands":
    ("control+e","$exec dmenu_run"),

}

MOD4_CONTROL_COMMANDS = {

"focus all":
    ("a","fullscreen disable $focus_all"),

"reload configuration":[
    ("r",'$exec "make -C ~/.i3 && i3-msg $no_border restart"'),
    ("Shift+r", '$exec "make -C ~/.i3 stable && i3-msg $no_border restart"')
],

"files":[
    ("f","exec $fm"),
    ("j","exec $fm Downloads")
],

"save layout":
    ("s",'exec "i3-save-tree > ~/.workspaces/stamp.json; emacsclient -create-frame --alternate-editor=\'\' ~/.workspaces/stamp.json"'),

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
],

}

MOD4_CONTROL_COMMANDS_RSB = {

"kill":
    ("w","kill"),

"cut":
    ("x","move container to workspace $wx"),

"paste":
    ("v",'$exec "i3-msg \'workspace --no-auto-back-and-forth $wx; move container to workspace $wx; workspace $wx\'"')
}

#TODO: maybe nested macros ar more readable?

MOD4_CONTROL_COMMANDS["move focused container to workspace and follow"] = []

def move_to_workspace(d,i):
    _, key = d
    MOD4_CONTROL_COMMANDS["move focused container to workspace and follow"].append(
        (key,"move container to workspace {}; workspace {}".format(i,i))
    )

forall(WORKSPACES, move_to_workspace)

DIRECTIONS = ["up","left","down","right"]

MOD4_COMMANDS_TO_SUPER_RSB = {}

def move_and_focus(d,i):
    MOD4_COMMANDS[i+" move"] = []
    MOD4_COMMANDS_TO_SUPER_RSB[i+" focus"] = []
    for j in range(len(d)):
        MOD4_COMMANDS[i+" move"].append(("Shift+"+d[j],"move "+DIRECTIONS[j]))
        MOD4_COMMANDS_TO_SUPER_RSB[i+" focus"].append((d[j],"focus "+DIRECTIONS[j]))

forall(ARROWS,move_and_focus)

def split_move(d,i):
    MOD4_CONTROL_COMMANDS[i+" split and move"] = []
    for j in range(len(d)):
        MOD4_CONTROL_COMMANDS[i+" split and move"].append(("Shift+"+d[j],"focus {}; split v; focus {}; move {}".format(DIRECTIONS[j],DIRECTIONS[(j+2)%4],DIRECTIONS[j])))

forall(ARROWS,split_move)

MOD4_COMMANDS_RSB["switch workspace"] = []

def switch_workspace(d,i):
    _, key = d
    MOD4_COMMANDS_RSB["switch workspace"].append(
        (key,"workspace {}".format(i))
    )

forall(WORKSPACES,switch_workspace)

#end python
