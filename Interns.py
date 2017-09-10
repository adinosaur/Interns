# -*- coding: UTF-8 –*-

PyIntInterns = {}
PyTupleInterns = {}

def obj_intern(o):
    obj_type = type(o)
    if obj_type is int:
        return int_intern(o)
    elif obj_type is str:
        return str_intern(o)
    elif obj_type is tuple:
        return tuple_intern(o)
    assert False

def int_intern(i):
    if type(i) is not int:
        return
    return PyIntInterns.setdefault(i, i)

def str_intern(s):
    if type(s) is not str:
        return
    return intern(s)

def tuple_intern(t):
    if type(t) is not tuple:
        return
    t2 = tuple([obj_intern(o) for o in t])
    assert t == t2
    return PyTupleInterns.setdefault(t2, t2)

if __name__ == "__main__":
    #test int obj intern
    with open("int.txt", "r") as f:
        print "int obj before intern:"
        intobjs = [int(l) for l in f.readlines()]
        for i in intobjs:
            print i, id(i)
        print "int obj after intern:"
        intobjs = [obj_intern(i) for i in intobjs]
        for i in intobjs:
            print i, id(i)
    
    #test str obj intern
    with open("str.txt", "r") as f:
        print "str obj before intern:"
        strobjs = [str(l).strip() for l in f.readlines()]
        for s in strobjs:
            print s, id(s)
        print "str obj after intern:"
        strobjs = [obj_intern(s) for s in strobjs]
        for s in strobjs:
            print s, id(s)
    
    #test tuple obj intern
    with open("tuple.txt", "r") as f:
        print "tuple obj before intern:"
        tupleobjs = [eval(l) for l in f.readlines()]
        for t in tupleobjs:
            print t, id(t)
        print "tuple obj after intern:"
        tupleobjs = [obj_intern(t) for t in tupleobjs]
        for t in tupleobjs:
            print t, id(t)