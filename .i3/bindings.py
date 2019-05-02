#include "commands.py"
#include "modes.py"
#include "keys.py"
#begin python

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
    if after_mode:
        _, _, pre, post, _, _, _, _ = ALLMODES[after_mode]
        if post != "" and y != "": y += "; " + post
        if post != "" and y == "": y += post
        if pre != "" and y != "": y = pre + " " + y
        if pre != "" and y == "": y = pre
        if current_mode:
            _, _, _, _, exit, _, _, _ = ALLMODES[current_mode]
            if exit != "": y = exit + "; " + y
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

def BIND_MOD1_COMMANDS(mode_tag):
    string = ""
    string += BINDBLOCKS(ALT_COMMANDS_RSB,mode_tag,modifier="Mod1",postfix="$refresh_status_bar")
    return string
    
def BIND_MOD4_COMMANDS(mode_tag,modifier="Mod4"):
    string = ""
    string += BINDBLOCKS(DMENU_COMMANDS,mode_tag,"$wrt",modifier=modifier)
    string += BINDBLOCKS(SUPER_COMMANDS,mode_tag,modifier=modifier)
    string += BINDBLOCKS(SUPER_COMMANDS_RSB,mode_tag,modifier=modifier,postfix="$refresh_status_bar")
    string += BINDBLOCKS(SUPER_CONTROL_COMMANDS,mode_tag,modifier=modifier+"+control")
    string += BINDBLOCKS(SUPER_CONTROL_COMMANDS_RSB,mode_tag,modifier=modifier+"+control",postfix="$refresh_status_bar")
    return string

def BIND_MODES(mode_tag):
    string = ""
    K = [x for x in MODES if x != mode_tag]
    K.sort()
    for x in K:
        _, keys, _, _, _, _, _, _ = MODES[x]
        for k in keys:
            string += BIND((k,""),mode_tag,x)
    K = [x for x in SUBMODES if x != mode_tag]
    K.sort()
    for x in K:
        _, keys, _, _, _, _, _, _ = SUBMODES[x]
        for k in keys:
            string += BIND(("Mod4+"+k,""),mode_tag,x)
    return string

USED_KEYS = {}

for x in ALLMODES.keys():
    USED_KEYS[x] = []

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

def MAKE_MODE(mode_tag):
    _, _, _, _, _, options, after_mode, free_keys = ALLMODES[mode_tag]
    string = " mode "+mode_tag+" {\n"
    if len(options):
        string += BINDBLOCKS({"options":options},mode_tag,after_mode)
    string += BIND_MODES(mode_tag)
    string += BINDBLOCKS(TOP_COMMANDS,mode_tag,"$wrt")
    string += BIND_MOD4_COMMANDS(mode_tag)
    string += LOCK(mode_tag,free_keys)
    string += " }"
    return string

def MAKE_SUPER_MODE():
    string = " mode $sup {\n"
    string += "\n # # # # # # # MODES # # # # # # #\n\n"
    string += BIND_MODES("$sup")
    string += "\n # # # # # # COMMANDS# # # # # # #\n\n"
    string += BIND(('"Super_L"',"fullscreen disable $exec $focus_one"),"$sup")
    string += BINDBLOCKS(TOP_COMMANDS,"$sup","$hov")
    string += BINDBLOCKS(ALT_COMMANDS_RSB,"$sup",modifier="Mod1",postfix="$refresh_status_bar")
    string += BINDBLOCKS(DMENU_COMMANDS,"$sup","$wrt")
    string += BINDBLOCKS(SUPER_COMMANDS,"$sup")
    string += BINDBLOCKS(SUPER_COMMANDS_RSB,"$sup",postfix="$refresh_status_bar")
    string += BINDBLOCKS(SUPER_CONTROL_COMMANDS,"$sup",modifier="control")
    string += BINDBLOCKS(SUPER_CONTROL_COMMANDS_RSB,"$sup",modifier="control",postfix="$refresh_status_bar")
    string += "\n # # # # # MOD4-COMMANDS # # # # #\n\n"
    string += BIND_MOD4_COMMANDS("$sup")
    string += "\n # # # # # # # LOCKS # # # # # # #\n\n"
    string += LOCK("$sup",ARROWS["default"]+['"Alt_L"'])
    string += LOCK_SHIFT("$sup")
    string += " }"
    return string

def MAKE_HOVER_MODE():
    string = " mode $hov {\n"
    string += "\n # # # # # # # MODES # # # # # # #\n\n"
    string += BIND_MODES("$hov")
    string += "\n # # # # # # COMMANDS# # # # # # #\n\n"
    string += BINDBLOCKS(TOP_COMMANDS,"$hov")
    string += BINDBLOCKS(ALT_COMMANDS_RSB,"$hov",modifier="Mod1",postfix="$refresh_status_bar")
    string += BIND_MOD4_COMMANDS("$hov")
    string += "\n # # # # # # # LOCKS # # # # # # #\n\n"
    string += LOCK("$hov",ARROWS["default"]+['"Alt_L"',"BackSpace",'"Control_L"','"Shift_L"',"space","Return","Tab","Menu"])
    string += LOCK_SHIFT("$hov",ARROWS["default"])
    string += " }"
    return string

#end python
