#include "forall.py"
#include "arrows.py"
#include "workspaces.py"
#begin python

TOP_COMMANDS={

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
    ("--release Mod4+Shift+Print","$exec i3-scrot -s"), # not working
],

"display": #TODO
    ("XF86Display", "$exec xrandr --output eDP1 --mode 1920x1080 --preferred"),

"borders":
    ("--border button2","$no_border"),

}

MOD1_COMMANDS_RSB={

"kill":
    ("F4","kill"),

}

MOD4_COMMANDS = {

"open terminal":
    ("Return","exec gnome-terminal"),

"open emacs":
    ("e","exec $emacs"),

"fullscreen":
    ("f","fullscreen toggle"),

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

}

MOD4_CONTROL_COMMANDS = {

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

"move container while browsing workspaces":[
    ("Tab","move container to workspace next; workspace next"),
    ("Shift+Tab","move container to workspace prev; workspace prev"),
    # ("j","move container to workspace prev; workspace prev"),
    # ("agrave","move container to workspace next; workspace next"),
    ("Home","move container to workspace prev; workspace prev"),
    ("End","move container to workspace next; workspace next"),
    ("ugrave","move container to workspace back_and_forth; workspace back_and_forth"),
],

}

MOD4_COMMANDS_TO_SUPER_RSB = {

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

MOD4_CONTROL_COMMANDS["move focused container to workspace and follow"] = []

def move_to_workspace(d,i):
    _, key = d
    MOD4_CONTROL_COMMANDS["move focused container to workspace and follow"].append(
        (key,"move container to workspace {}; workspace {}".format(i,i))
    )

forall(WORKSPACES, move_to_workspace)

MOD4_CONTROL_COMMANDS_TO_SUPER_RSB = {

"kill":
    ("w","kill"),

"cut":
    ("x","move container to workspace $wx"),

"paste":
    ("v",'$exec "i3-msg \'workspace --no-auto-back-and-forth $wx; move container to workspace $wx; workspace $wx\'"')
}

DIRECTIONS = ["up","left","down","right"]

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

MOD4_COMMANDS_TO_SUPER_RSB["switch workspace"] = []

def switch_workspace(d,i):
    _, key = d
    MOD4_COMMANDS_TO_SUPER_RSB["switch workspace"].append(
        (key,"workspace {}".format(i))
    )

forall(WORKSPACES,switch_workspace)

MOD4_COMMANDS_RSB = {

"where am i?":
    ('x',"$border, $focus_one, fullscreen disable"),

}

MOD4_COMMANDS_TO_SUPER = {

"here i am!":
    ("Shift+x","$no_border"),

"application menu":
    ("Menu","exec morc_menu"),

}

MOD4_COMMANDS_TO_DEFLT = {

"start dmenu for applications":
    ("Shift+exclam","$exec $dmenu"),

"start dmenu for commands":
    ("control+e","$exec dmenu_run"),

}

#end python
