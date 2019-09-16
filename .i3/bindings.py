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

def BIND((x,y),current_mode=None,after_mode=None,postfix=""):

    if postfix != "":
        if y != "":
            y += "; " + postfix
        else:
            y += postfix

    if current_mode:
        if after_mode and current_mode != after_mode:

            _, _, after_specs = MODES[after_mode]
            _, _, current_specs = MODES[current_mode]

            if y != "":
                y = "mode " + after_mode + " " + y
            else:
                y = "mode " + after_mode

            if "style" in after_specs:
                y += ", " + after["style"]

            y += "; $exec $alert " + after_mode

            if "exec_on_exit" in current_specs:
                y += " && " + current_specs["exec_on_exit"]

            if "exec_on_enter" in after_specs:
                y += " && " + after_specs["exec_on_enter"]

        USED_KEYS[current_mode].append(x)

    return " bindsym {} {}\n".format(x,y)

def BINDBLOCK(d,name,current_mode=None,after_mode=None,postfix=""):
    string = " # {}\n".format(name)
    if type(d) == tuple:
        string += BIND(d,current_mode,after_mode,postfix)
    elif type(d) == list:
        for t in d:
            string += BIND(t,current_mode,after_mode,postfix)
    return string + "\n"

def BINDALL(obj,fun,**kwargs):
    string = ""
    keys = obj.keys()
    keys.sort()
    for i in keys:
        string += fun(obj[i],i,**kwargs)
    return string

def BINDBLOCKS(blocks,current_mode=None,after_mode=None,postfix=""):
    return BINDALL(blocks,BINDBLOCK,current_mode=current_mode,after_mode=after_mode,postfix=postfix)

def BIND_COMMANDS(mode_tag):
    string = ""
    string += BINDBLOCKS(COMMANDS,mode_tag)
    string += BINDBLOCKS(COMMANDS_TO_DEFLT,mode_tag,"$def")
    string += BINDBLOCKS(COMMANDS_TO_WRITE,mode_tag,"$wrt")
    return string

def BIND_MOD1_COMMANDS(mode_tag):
    string = ""
    string += BINDBLOCKS(MOD1_COMMANDS_RSB,mode_tag,postfix="$refresh_status_bar")
    return string

def BIND_MOD4_COMMANDS(mode_tag):
    string = ""
    string += BINDBLOCKS(MOD4_COMMANDS,mode_tag)
    string += BINDBLOCKS(MOD4_COMMANDS_TO_WRITE,mode_tag,"$wrt")
    string += BINDBLOCKS(MOD4_COMMANDS_RSB,mode_tag,postfix="$refresh_status_bar")
    return string

def BIND_TO_MODE(mode,after_mode,current_mode=""):
    string = ""
    if current_mode != "" and current_mode != after_mode:
        _, keys, _ = mode
        for key in keys:
            string += BIND((key,""),current_mode,after_mode)
    return string

def BIND_MODES(mode_tag):
    return BINDALL(MODES,BIND_TO_MODE,current_mode=mode_tag) + "\n"

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

    _, _, specs = MODES[mode_tag]

    string = " mode "+mode_tag+" {\n\n"

    if "options" in specs:
        if "after_mode" in specs:
            after_mode = specs["after_mode"]
        else:
            after_mode= ""
        string += BINDBLOCK(specs["options"],mode_tag,after_mode)

    string += BIND_MODES(mode_tag)
    string += BIND_COMMANDS(mode_tag)
    string += BIND_MOD1_COMMANDS(mode_tag)
    string += BIND_MOD4_COMMANDS(mode_tag)
    string += LOCK(mode_tag)

    string += " }"

    return string

#end python
