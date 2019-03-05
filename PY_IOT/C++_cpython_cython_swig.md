
#Wrapping C/C++ for Python

### A. Manual Wrapping

#### *https://intermediate-and-advanced-software-carpentry.readthedocs.io/en/latest/c++-wrapping.html*
`
char * hello(char * what)
# 1. Python-callable function that takes in a string and returns a string.
static PyObject * hello_wrapper(PyObject * self, PyObject * args)
{
  char * input;
  char * result;
  PyObject * ret;

  // parse arguments
  if (!PyArg_ParseTuple(args, "s", &input)) {
    return NULL;
  }

  // run the actual function
  result = hello(input);

  // build the resulting string into a Python object.
  ret = PyString_FromString(result);
  free(result);

  return ret;
}
# 2. register this function within a module’s symbol table 
static PyMethodDef HelloMethods[] = {
 { "hello", hello_wrapper, METH_VARARGS, "Say hello" },
 { NULL, NULL, 0, NULL }
};
# 3. init
DL_EXPORT(void) inithello(void)
{
  Py_InitModule("hello", HelloMethods);
}
# 4.  setup.py script:
from distutils.core import setup, Extension
# the c++ extension module
extension_mod = Extension("hello", ["hellomodule.c", "hello.c"])

setup(name = "hello", ext_modules=[extension_mod])
`

### B.   SWIG
http://www.swig.org/tutorial.html
http://www.swig.org/Doc1.3/Python.html

'''
SWIG stands for “Simple Wrapper Interface Generator”, and it is capable of wrapping C in a large variety of languages. To quote, “SWIG is used with different types of languages including common scripting languages such as Perl, PHP, Python, Tcl, Ruby and PHP. The list of supported languages also includes non-scripting languages such as C#, Common Lisp (CLISP, Allegro CL, CFFI, UFFI), Java, Modula-3 and OCAML. Also several interpreted and compiled Scheme implementations (Guile, MzScheme, Chicken) are supported.”
'''
# 1 Makefile:
all:
     swig -python -c++ -o _swigdemo_module.cc swigdemo.i
     python setup.py build_ext --inplace
## This shows the steps we need to run: first, run SWIG to generate the C code extension; then run setup.py build to actually build it.

## 2. SWIG wrapper file, ‘swigdemo.i’  
`
%module swigdemo

%{
#include <stdlib.h>
#include "hello.h"
%}

%include "hello.h"
`
## 3
`
from distutils.core import setup, Extension

extension_mod = Extension("_swigdemo", ["_swigdemo_module.cc", "hello.c"])

setup(name = "swigdemo", ext_modules=[extension_mod])
`


### C. Cython -  subset of python language
#### https://cython.org/
`
# Passing byte strings
from libc.stdlib cimport malloc
from libc.string cimport strcpy, strlen

cdef char* hello_world = 'hello world'
cdef Py_ssize_t n = strlen(hello_world)


cdef char* c_call_returning_a_c_string():
    cdef char* c_string = <char *> malloc((n + 1) * sizeof(char))
    if not c_string:
        raise MemoryError()
    strcpy(c_string, hello_world)
    return c_string


cdef void get_a_c_string(char** c_string_ptr, Py_ssize_t *length):
    c_string_ptr[0] = <char *> malloc((n + 1) * sizeof(char))
    if not c_string_ptr[0]:
        raise MemoryError()

    strcpy(c_string_ptr[0], hello_world)
    length[0] = n
`
 
### D. C-types
#### https://dbader.org/blog/python-ctypes-tutorial
#### https://docs.python.org/3/library/ctypes.html
`
>>> from ctypes import *
>>> print(windll.kernel32)  
<WinDLL 'kernel32', handle ... at ...>
>>> print(cdll.msvcrt)      
<CDLL 'msvcrt', handle ... at ...>
>>> libc = cdll.msvcrt      
>>>
##

>>> from ctypes import *
>>> libc.printf
<_FuncPtr object at 0x...>
>>> print(windll.kernel32.GetModuleHandleA)  
<_FuncPtr object at 0x...>
>>> print(windll.kernel32.MyOwnFunction)     
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "ctypes.py", line 239, in __getattr__
    func = _StdcallFuncPtr(name, self)
AttributeError: function 'MyOwnFunction' not found
>>>
#

/* ANSI version */
HMODULE GetModuleHandleA(LPCSTR lpModuleName);
/* UNICODE version */
HMODULE GetModuleHandleW(LPCWSTR lpModuleName);
`
## Examples->
### XML ->
