import os
from os import path
from distutils.ccompiler import new_compiler

# Input: student's file pass
# Output: 0 if not compile able, 1 if compile able.
def compileable_fun(inputfilepass):
    inputfilepass = '/home/tony/research/test.c'    # student submission path in database

    compiler = new_compiler()
    try:
        compiler.compile([inputfilepass])
        compiler.link_executable(['test.o'], 'test')
        #print("True1")
        return 1
    except:
        #print("False1")
        return 0
