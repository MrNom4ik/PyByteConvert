from types import CodeType

__title__= 'PyByteConvert'
__author__= 'Mr. Nom4ik'
__version__= '0.0.2'
# Github: https://github.com/MrNom4ik/PyByteConvert

class Code:
    def __init__(self, mode): self.args, self.message= (), mode
    def __repr__(self): return self.message.format(self.args)
    def add(self, arg): self.args+= (arg,)

class Encode:
    def __init__(self, message): self.message= message
    def __repr__(self): return f"{self.message.encode('cp500')}.decode('cp500')"

def get_args(obj, mode= 'lambda', encode= False, string= False):
    if string: obj= compile(obj, '<file>', 'exec')
    if isinstance(obj, CodeType):
        c= Code({'type': 'CodeType{}', 'lambda': 'type((lambda: 0).__code__){}' }.get(mode))
        for e in ['co_argcount', 'co_posonlyargcount', 'co_kwonlyargcount', 'co_nlocals', 'co_stacksize', 'co_flags', 'co_code', 'co_consts', 'co_names', 'co_varnames', 'co_filename', 'co_name', 'co_firstlineno', 'co_lnotab', 'co_freevars', 'co_cellvars']: # if you get an error about the length of the arguments, then update this list of arguments according to your version of python, the arguments are in the sequence of arguments of the CodeType class
            c.add(get_args(getattr(obj, e), mode, encode))
        return c
    elif isinstance(obj, tuple):
        return tuple([get_args(e, mode, encode) for e in obj])
    elif isinstance(obj, str) and encode: return Encode(obj)
    else: return obj
