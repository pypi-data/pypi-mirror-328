import os
import re
import sys
import shutil
import subprocess
import numpy

from setuptools import setup, find_packages, Extension
from setuptools.command.install import install
from setuptools.command.build_ext import build_ext as _build_ext

try:
    from Cython.Build import cythonize
    CYTHON_INSTALLED = True
except ImportError:
    CYTHON_INSTALLED = False

NAME = "deepquant"

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

def replace_folder(src, dst):
    if os.path.exists(dst):
        shutil.rmtree(dst)
    shutil.copytree(src, dst)

def get_git_tag():
    #try:
        #r = subprocess.run(["git tag --sort=-creatordate | head -n 1"], shell=True, capture_output=True, text=True)
        #git_tag = r.stdout.strip()
        tag_re = re.compile("^\d+.\d+.\d+$")
        r = subprocess.check_output("git tag --sort=-creatordate", text=True, shell=True)
        git_tags = r.split("\n")
        for tag in git_tags:
            if len(tag_re.findall(tag)) == 1:
                #subprocess.run(["echo", tag, ">", "./ver.temp"], shell=True)
                os.system(f"echo {tag}> ./ver.temp")
                return tag
        else:
            return '0.0.1'
    #except Exception:
    #    return '0.1.0'

package_data = {}
if sys.platform.startswith('win'):
    replace_folder("resources/swordfish_tmp/swordfish", "deepquant/oplib")
    package_data = {
        NAME: [
            "oplib/tzdb/*",
        ]
    }
elif sys.platform.startswith("linux"):
    replace_folder("resources/swordfish_tmp/swordfish", "deepquant/oplib")
    replace_folder("resources/swordfish_tmp/swordfish.libs", "deepquant/swordfish.libs")
    package_data = {
        NAME: [
            "oplib/tzdb/*",
            "swordfish.libs/*",
        ]
    }
else:
    print(f"not support os.name: {sys.platform}")

ext_modules = []
if CYTHON_INSTALLED:
    ext_modules.append(
        Extension(
            "deepquant.quest.mod.mod_quant_data.data_sources.tight_loops", 
            ["deepquant/quest/mod/mod_quant_data/data_sources/tight_loops.pyx"],
            include_dirs=[numpy.get_include()]
        )
    )
else:
    ext_modules.append(
        Extension("deepquant.quest.mod.mod_quant_data.data_sources.tight_loops", ["deepquant/quest/mod/mod_quant_data/data_sources/tight_loops.c"])
    )

class CustomInstall(install):

    def run(self):
        install.run(self)

setup(
    name=NAME,
    #version="0.1.0",
    version=get_git_tag(),
    author="cgs",
    description="quant data and factor tools by cgs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    # url="https://github.com/yourusername/your-repository",
    packages=[
        "deepquant", 
        "deepquant.quest",
        "deepquant.data", 
        "deepquant.factor",
        "deepquant.oplib",
        "deepquant.samples",
        "deepquant.data.gqclient",
        "deepquant.data.utils",
        "deepquant.data.interface",
        "deepquant.data.proto",
        "deepquant.docs",
        "deepquant.examples",
    ],
    ext_modules=cythonize(ext_modules, language_level="3") if CYTHON_INSTALLED else ext_modules,
    package_data=package_data,
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=[
        "requests>=2.25.1",
        "numpy>=1.19.5,<=1.26.4",
        "pandas>=1.2.0",
        "websocket-client",
        "protobuf<=3.20.3",
        "PyJWT",
        "statsmodels",
        "scipy",
        "pyecharts",
        "empyrical-reloaded",
        "astor",
        "RestrictedPython",
        "pyyaml",
        "hdf5plugin==5.0.0",
        "tqdm==4.67.1",
        "lru-dict==1.3.0",
        "logbook",
        "jsonpickle",
        "methodtools",
        "tabulate",
        "tqdm",
        "hdf5plugin",
        "lru-dict",
        "matplotlib"
    ],
    extras_require={
        "dev": [
            "pytest>=6.2.2",
            "sphinx>=3.4.3",
        ],
    },
)
