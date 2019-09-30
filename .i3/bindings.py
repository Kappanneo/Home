#include "commands.py"
#include "modes.py"
#include "keys.py"
#begin python

def SET(X):
    string=""
    I = X.keys()
    I.sort()
    for i in I:
        string += " set {} {}\n".format(i,X[i]["name"])
    return string

def BIND((x,y),current_mode=None,after_mode=None,postfix=None):

    if postfix:
        if y != "":
            y += "; " + postfix

    if current_mode:

        if after_mode and current_mode != after_mode:

            if y != "":
                y = "mode " + after_mode + " " + y + "; $exec $alert " + after_mode
            else:
                y = "mode " + after_mode + "; $exec $alert " + after_mode

            if "exec_on_exit" in  MODES[current_mode]:
                y += " && " + MODES[current_mode]["exec_on_exit"]

            if "exec_on_enter" in MODES[after_mode]:
                y += " && " + MODES[after_mode]["exec_on_enter"]

        if x not in USED_KEYS[current_mode]: USED_KEYS[current_mode] += [x]

        else: return "# WARNING: key already taken for command:\n# bindsym {} {}\n".format(x,y)

    return " bindsym {} {}\n".format(x,y)

def BINDBLOCK(d,name,current_mode=None,after_mode=None,postfix=None):
    if current_mode:
        string = " # {}: {}\n".format(current_mode,name)
    else:
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

def BINDBLOCKS(blocks,current_mode=None,after_mode=None,postfix=None):
    return BINDALL(blocks,BINDBLOCK,current_mode=current_mode,after_mode=after_mode,postfix=postfix)

def BIND_TOP_COMMANDS(mode_tag):
    string = ""
    string += BINDBLOCKS(TOP_COMMANDS,mode_tag)
    return string

def BIND_MOD1_COMMANDS(mode_tag):
    string = ""
    string += BINDBLOCKS(MOD1_COMMANDS_TO_DEFLT,mode_tag,"$def")
    string += BINDBLOCKS(MOD1_COMMANDS_RSB,mode_tag,postfix="$refresh_status_bar")
    return string

def BIND_MOD4_COMMANDS(mode_tag):
    string = ""
    string += BINDBLOCKS(MOD4_COMMANDS,mode_tag)
    string += BINDBLOCKS(MOD4_COMMANDS_RSB,mode_tag,postfix="$refresh_status_bar")
    string += BINDBLOCKS(MOD4_COMMANDS_TO_DEFLT,mode_tag,"$def")
    string += BINDBLOCKS(MOD4_COMMANDS_TO_RIGHT,mode_tag,"$rgh")
    string += BINDBLOCKS(MOD4_COMMANDS_TO_RIGHT_RSB,mode_tag,"$rgh",postfix="$refresh_status_bar")
    return string

def TO_MODE(AFTER_MODE,after_mode,current_mode=None):
    string = ""
    if current_mode and current_mode != after_mode and "keys" in AFTER_MODE:
        for key in AFTER_MODE["keys"]:
            string += BIND((key,""),current_mode,after_mode)
    return string

def BIND_MODES(mode_tag):
    string = " # {}: exit to other mode\n".format(mode_tag)
    string += BINDALL(MODES,TO_MODE,current_mode=mode_tag)
    string += "\n"
    return string

USED_KEYS = {}

for x in MODES.keys():
    USED_KEYS[x] = []

def LOCK(mode):
    string = "";
    U = [(x,"nop") for x in KEYS if x not in USED_KEYS[mode]]
    if len(U): string += BINDBLOCKS({"{}: lock unused keys".format(mode):U})
    return string

def FREE(mode,free_keys):
    USED_KEYS[mode] += free_keys
    return ""

def LOCK_SHIFT(mode):
    string = "";
    U = [(x,"nop") for x in ['Shift+'+y for y in SHIFT_KEYS] if x not in USED_KEYS[mode]]
    if len(U): string += BINDBLOCKS({"{}: lock unused Shift+keys (since Shift is free)".format(mode):U})
    return string

def FREE_SHIFT(mode,free_keys):
    USED_KEYS[mode] += ['Shift'+y for y in free_keys]
    return ""

def MAKE_MODE(mode_tag):

    string = " mode "+mode_tag+" {\n\n"

    if "options" in MODES[mode_tag]:

        if "after_mode" in MODES[mode_tag]:
            after_mode = MODES[mode_tag]["after_mode"]
        else:
            after_mode= None

        string += BINDBLOCK(MODES[mode_tag]["options"],"options",mode_tag,after_mode)

    string += BIND_MODES(mode_tag)
    string += BIND_TOP_COMMANDS(mode_tag)
    string += BIND_MOD1_COMMANDS(mode_tag)
    string += LOCK(mode_tag)

    string += " }"

    return string

#end python
