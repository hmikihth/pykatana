import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "pykatana",
    version = "0.0.1",
    author = "Miklos Horvath",
    author_email = "hmiki@blackpantheros.eu",
    description = ("A python source-cutter tool"),
    license = "GPL3",
    keywords = "source cutting tool",
    packages=['pykatana'],
    scripts=['usr/bin/pykatana'],
    long_description=read('README'),
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Topic :: Utilities",
        "Environment :: Console",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3",
    ],
)
