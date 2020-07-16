# Compilation:
# Dependencies in c folder: run_cython.c
# python setup.py build_ext --inplace

from distutils.core import setup
from Cython.Build import cythonize

setup(ext_modules = cythonize('run_cython.pyx'))
