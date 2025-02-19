import os
from setuptools import setup, find_packages

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="opaque",
    version="1.0.0",
    author="Stefan Marsiske",
    author_email="pyopaque@ctrlc.hu",
    description="python libopaque wrapper",
    license="GPLv3",
    keywords="cryptography API libopaque OPAQUE PAKE AKE key-exchange",
    url="https://github.com/stef/libopaque",
    packages=find_packages(),
    long_description=read('README.md'),
    long_description_content_type="text/markdown",
    requires=["libsodium"],
    install_requires = ("pysodium"),
    classifiers=["Development Status :: 4 - Beta",
                 "License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)",
                 "Topic :: Security :: Cryptography",
                 "Topic :: Security"],
)
