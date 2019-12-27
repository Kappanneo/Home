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
    ("XF86ScreenSaver","$exec $screen_off"),

"screenshot":
    ("Print","$exec i3-scrot"),

"display": #TODO
    ("XF86Display", "$exec xrandr --output eDP1 --mode 1920x1080 --preferred"),

"middle mouse no border":
    ("--border button2","$no_border"),
}

MOD1_COMMANDS = {}

MOD1_COMMANDS_RSB = {

"kill":
    ("Mod1+F4","kill"),
}

MOD4_COMMANDS_DEFLT = {

"start dmenu for applications":
    ("Mod4+Shift+exclam","$exec $dmenu"),

"start dmenu for commands":
    ("Mod4+control+e","$exec dmenu_run"),

"reload configuration":[
    ("Mod4+control+r",'$exec "make -C ~/.i3 && i3-msg $no_border restart"'),
    ("Mod4+control+Shift+r", '$exec "make -C ~/.i3 stable && i3-msg $no_border restart"')
],

}

MOD4_COMMANDS = {

"xkill":
    ("Mod4+q","--release $exec xkill"),

"touchpad":[
    ("Mod4+space","$exec $touchpad_x_on"),
    ("Mod4+Shift+space","$exec $touchpad_x_off"),
],

"fullscreen":[
    ("Mod4+f","fullscreen toggle"),
    ("Mod4+Shift+f",'$exec "sleep 0.5; xdotool key F11"'),
],

"split orientation":[
    ("Mod4+v","split v; $exec notify-send 'vertical'"),
    ("Mod4+h","split h; $exec notify-send 'horizontal'"),
    ("Mod4+g","split v; focus parent; layout toggle split; focus child"),
],

"application menu":
    ("Mod4+Menu","$exec morc_menu"),

"resize window":[
    ("Mod4+i","resize shrink height 5 px or 5 ppt"),
    ("Mod4+p","resize  grow  height 5 px or 5 ppt"),
    ("Mod4+Prior","resize shrink height 5 px or 5 ppt"),
    ("Mod4+Next", "resize  grow  height 5 px or 5 ppt"),
    ("Mod4+Shift+i","resize shrink width  5 px or 5 ppt"),
    ("Mod4+Shift+p","resize  grow  width  5 px or 5 ppt"),
    ("Mod4+Shift+Prior","resize shrink width  5 px or 5 ppt"),
    ("Mod4+Shift+Next", "resize  grow  width  5 px or 5 ppt"),
],

"resize (precise)":[
    ("Mod4+control+i","resize shrink height 1 px or 1 ppt"),
    ("Mod4+control+p","resize  grow  height 1 px or 1 ppt"),
    ("Mod4+control+Prior","resize shrink height 1 px or 1 ppt"),
    ("Mod4+control+Next", "resize  grow  height 1 px or 1 ppt"),
    ("Mod4+control+Shift+i","resize shrink width  1 px or 1 ppt"),
    ("Mod4+control+Shift+p","resize  grow  width  1 px or 1 ppt"),
    ("Mod4+control+Shift+Prior","resize shrink width  1 px or 1 ppt"),
    ("Mod4+control+Shift+Next", "resize  grow  width  1 px or 1 ppt"),
],

"resize (scale)":[
    ("Mod4+control+minus","resize shrink height 5 px or 5 ppt; resize shrink width  5 px or 5 ppt"),
    ("Mod4+control+plus","resize  grow  height 5 px or 5 ppt; resize  grow  width  5 px or 5 ppt"),
    ("Mod4+control+Shift+minus","resize shrink height 1 px or 1 ppt; resize shrink width  1 px or 1 ppt"),
    ("Mod4+control+Shift+plus","resize  grow  height 1 px or 1 ppt; resize  grow  width  1 px or 1 ppt"),
],

}

MOD4_COMMANDS_RSB = {

"kill":
    ("Mod4+control+w","kill"),

"cut":
    ("Mod4+control+x","move container to workspace $wx"),

"paste":
    ("Mod4+control+v",'$exec "i3-msg \'workspace --no-auto-back-and-forth $wx; move container to workspace $wx; workspace $wx\'"'),

"browse workspaces":[
    ("Mod4+Tab","workspace next"),
    ("Mod4+Shift+Tab","workspace prev"),
    ("Mod4+j","workspace prev"),
    ("Mod4+agrave","workspace next"),
    ("Mod4+Home","workspace prev"),
    ("Mod4+End","workspace next"),
    ("Mod4+ugrave","workspace back_and_forth"),
],

"focus and border":[
    ("Mod4+x","fullscreen disable $border $focus_one"),
    ("Mod4+Shift+x","$no_border"),
    ("Mod4+less","focus child"),
    ("Mod4+Shift+greater","focus parent"),
    ("Mod4+control+a","fullscreen disable $focus_all"),
],

"open terminal":
    ("Mod4+Return","$exec gnome-terminal"),

"open emacs":
    ("Mod4+e","$exec $emacs"),

"shutdown emacs server":
    ("Mod4+control+Shift+e","$exec pkill emacs"),

"file manager":[
    ("Mod4+control+f","$exec $fm"),
    ("Mod4+control+j","$exec $fm Downloads")
],

"save layout":
    ("Mod4+control+s",'$exec "i3-save-tree > ~/.workspaces/stamp.json; emacsclient -create-frame --alternate-editor=\'\' ~/.workspaces/stamp.json"'),

}

MOD4_COMMANDS["move focused container to workspace"] = []
MOD4_COMMANDS_RSB["switch workspace"] = []

def workspace_commands(X,i):
    key = X["key"]
    MOD4_COMMANDS["move focused container to workspace"].append(("Mod4+control+"+key,"move container to workspace {}".format(i)))
    MOD4_COMMANDS_RSB["switch workspace"].append(("Mod4+"+key,"workspace {}".format(i)))

forall(WORKSPACES,workspace_commands)

DIRECTIONS = ["up","left","down","right"]

DEFLT = ARROW_SETS["default"]
LEFT  = ARROW_SETS["wasd"]
RIGHT = ARROW_SETS["oklò"]

MOD4_COMMANDS["default move"] = []
MOD4_COMMANDS["default split and move"] = []
MOD4_COMMANDS_RSB["default focus"] = []

MOD4_COMMANDS["wasd move"] = []
MOD4_COMMANDS["wasd split and move"] = []
MOD4_COMMANDS_RSB["wasd focus"] = []

MOD4_COMMANDS["oklò move"] = []
MOD4_COMMANDS["oklò split and move"] = []
MOD4_COMMANDS_RSB["oklò focus"] = []

for i in range(len(DIRECTIONS)):

    MOD4_COMMANDS["default move"].append(("Mod4+Shift+"+DEFLT[i],"move "+DIRECTIONS[i]))
    MOD4_COMMANDS["default split and move"].append(("Mod4+control+Shift+"+DEFLT[i],"focus {}; split v; focus {}; move {}".format(DIRECTIONS[i],DIRECTIONS[(i+2)%4],DIRECTIONS[i])))
    MOD4_COMMANDS_RSB["default focus"].append(("Mod4+"+DEFLT[i],"focus "+DIRECTIONS[i]))

    MOD4_COMMANDS["wasd move"].append(("Mod4+Shift+"+LEFT[i],"move "+DIRECTIONS[i]))
    MOD4_COMMANDS["wasd split and move"].append(("Mod4+control+Shift+"+LEFT[i],"focus {}; split v; focus {}; move {}".format(DIRECTIONS[i],DIRECTIONS[(i+2)%4],DIRECTIONS[i])))
    MOD4_COMMANDS_RSB["wasd focus"].append(("Mod4+"+LEFT[i],"focus "+DIRECTIONS[i]))

    MOD4_COMMANDS["oklò move"].append(("Mod4+Shift+"+RIGHT[i],"move "+DIRECTIONS[i]))
    MOD4_COMMANDS["oklò split and move"].append(("Mod4+control+Shift+"+RIGHT[i],"focus {}; split v; focus {}; move {}".format(DIRECTIONS[i],DIRECTIONS[(i+2)%4],DIRECTIONS[i])))
    MOD4_COMMANDS_RSB["oklò focus"].append(("Mod4+"+RIGHT[i],"focus "+DIRECTIONS[i]))

#end python
