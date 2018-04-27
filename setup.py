from distutils.core import setup
import numpy as np
from Cython.Build import cythonize

setup(
  name = 'Dijkstra Maps',
  ext_modules = cythonize("dijkstra_map.pyx", annotate=True),
  include_dirs=[np.get_include()]
)
