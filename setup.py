from distutils.core import setup
from codecs import open
from os import path

import numpy as np
from Cython.Build import cythonize

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='Dijkstra Maps',
    varsion='0.0.1',
    description="Dijkstra Maps for Distance in Tile Based Games",
    long_description=long_description,
    url='https://github.com/madrury/dijkstra-maps',
    author='Matthew Drury',
    author_email='matthew.drury.83@gmail.com',
    ext_modules=cythonize("src/dijkstra_map.pyx", annotate=True),
    include_dirs=[np.get_include()],
    packages=['src'],
    install_requires=['numpy', 'cython']
)
