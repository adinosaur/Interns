# -*- coding: UTF-8 –*-

PyIntInterns = {}
PyStrInterns = {}
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
    if -5 <= i <= 256:
        return
    return PyIntInterns.setdefault(i, i)

def str_intern(s):
    if type(s) is not str:
        return
    if len(s) <= 1:
        return
    #return intern(s)
    return PyStrInterns.setdefault(s, s)

def tuple_intern(t):
    if type(t) is not tuple:
        return
    if len(t) == 0:
        return
    t2 = tuple([obj_intern(o) for o in t])
    assert t == t2
    return PyTupleInterns.setdefault(t2, t2)

if __name__ == "__main__":
    pass