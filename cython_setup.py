from distutils.core import setup
from Cython.Build import cythonize
import numpy

setup(name="LebwohlLasher_cython",
      ext_modules=cythonize("LebwohlLasher_cython.pyx",language_level=3), include_dirs=[numpy.get_include()])