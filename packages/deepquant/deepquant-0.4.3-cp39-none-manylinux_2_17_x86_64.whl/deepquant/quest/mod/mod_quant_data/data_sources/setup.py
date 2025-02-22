# -*- coding: utf-8 -*-
"""
生成对应版本的pyd文件
命令：python setup.py build_ext --inplace
"""
import numpy as np
from setuptools import Extension, setup
from Cython.Build import cythonize

extensions = [
    Extension(
        "tight_loops",
        ["tight_loops.pyx"],
        include_dirs=[np.get_include()],
    ),
]

setup(
    ext_modules=cythonize(extensions)
)
