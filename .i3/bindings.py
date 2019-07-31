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
    if after_mode and current_mode != after_mode:
        _, _, pre, post, _, _, _, _, _, _ = MODES[after_mode]
        if post != "" and y != "": y += "; " + post
        if post != "" and y == "": y += post
        if pre != "" and y != "": y = pre + " " + y
        if pre != "" and y == "": y = pre
        if current_mode:
            _, _, _, _, exit, _, _, _, _, _ = MODES[current_mode]
            if exit != "": y = exit + "; " + y
    return " bindsym {} {}; $exec echo {} >> .i3/log\n".format(x,y,x)

def BINDBLOCK(d,name,current_mode=None,after_mode=None,modifier="",prefix="",postfix=""):
    string = " # {}\n".format(name)
    if type(d) == tuple:
        string += BIND(d,current_mode,after_mode,modifier,prefix,postfix)
    elif type(d) == list:
        for t in d:
            string += BIND(t,current_mode,after_mode,modifier,prefix,postfix)
    return string + "\n"

def BINDALL(obj,fun,**kwargs):
    string = ""
    keys = obj.keys()
    keys.sort()
    for i in keys:
        string += fun(obj[i],i,**kwargs)
    return string

def BINDBLOCKS(blocks,current_mode=None,after_mode=None,modifier="",prefix="",postfix=""):
    return BINDALL(blocks,BINDBLOCK,current_mode=current_mode,after_mode=after_mode,modifier=modifier,prefix=prefix,postfix=postfix)

def BIND_TOP_COMMANDS(mode_tag):
    string = ""
    string += BINDBLOCKS(TOP_COMMANDS,mode_tag)
    string += BINDBLOCKS(TOP_COMMANDS_TO_HOVER,mode_tag,"$hov")
    return string

def BIND_ALT_COMMANDS(mode_tag,modifier="Mod1"):
    string = ""
    string += BINDBLOCKS(ALT_COMMANDS_RSB,mode_tag,modifier=modifier,postfix="$refresh_status_bar")
    return string
    
def BIND_SUPER_COMMANDS(mode_tag,modifier="Mod4"):
    string = ""
    string += BINDBLOCKS(SUPER_COMMANDS,mode_tag,modifier=modifier)
    string += BINDBLOCKS(SUPER_CONTROL_COMMANDS,mode_tag,modifier=modifier+"+control")
    string += BINDBLOCKS(SUPER_COMMANDS_TO_WRITE,mode_tag,"$wrt",modifier=modifier)
    string += BINDBLOCKS(SUPER_COMMANDS_TO_HOVER,mode_tag,"$hov",modifier=modifier)
    string += BINDBLOCKS(SUPER_COMMANDS_TO_TOUCH,mode_tag,"$tch",modifier=modifier)
    string += BINDBLOCKS(SUPER_COMMANDS_TO_HOVER_RSB,mode_tag,"$hov",modifier=modifier,postfix="$refresh_status_bar")
    string += BINDBLOCKS(SUPER_CONTROL_COMMANDS_TO_HOVER_RSB,mode_tag,"$hov",modifier=modifier+"+control",postfix="$refresh_status_bar")
    return string

def BIND_TO_MODE(d,after_mode,current_mode="",modifier="",free_keys=[]):
    string = ""
    if current_mode == "" or current_mode == after_mode:
        return string
    else:
        _, keys, _, _, _, _, _, _, _, _ = d
        for key in [x for x in keys if x not in free_keys]:
            if modifier != "":
                key = modifier + "+" + key
            string += BIND((key,""),current_mode,after_mode)
        return string + "\n"

def BIND_MODES(mode_tag,free_keys=[]):
    return BINDALL(MODES,BIND_TO_MODE,current_mode=mode_tag,free_keys=free_keys)

USED_KEYS = {}

for x in MODES.keys():
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
    _, _, _, _, _, options, after_mode, modifier, free_keys, free_shift_keys = MODES[mode_tag]
    string = " mode "+mode_tag+" {\n\n"
    if len(options):
        string += BINDBLOCKS({"options":options},mode_tag,after_mode,modifier=modifier)
    string += BIND_MODES(mode_tag,free_keys)
    string += BIND_TOP_COMMANDS(mode_tag)
    string += BIND_ALT_COMMANDS(mode_tag)
    string += BIND_SUPER_COMMANDS(mode_tag)
    string += LOCK(mode_tag,free_keys)
    if len([x for x in ['"Shift_L"','"Shift_R"'] if x in free_keys]):
        string += LOCK_SHIFT(mode_tag,free_shift_keys)
    string += " }"
    return string

#end python
