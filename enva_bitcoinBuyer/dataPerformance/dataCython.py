# BitcoinBuyer program tools:
# Thomas Maestas
# Cython utilities
# Dependencies: venva ENV: cython,

""" vars:
cdef int a,b,c
cdef char *s
cdef float x = 0.5 (single precision)
cdef double x = 63.4 (double precision)
cdef list names
cdef dict goals_for_each_play
cdef object card_deck
    functions:
def python only
cdef cython only (must be called from within Cython)
cpdef C and Python.
"""
def test(x):
    y = 1
    for i in range(1, x+1):
        y *= i
    return y
"""
cpdef int test(int x):
    cdef int y = 1
    cdef int i
    for i in range(1, x+1):
        y *= i
    return y
"""

