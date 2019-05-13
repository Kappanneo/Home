#begin python

def forall(obj,fun):
    keys = obj.keys()
    keys.sort()
    for i in keys:
        fun(obj[i],i)

#end python
