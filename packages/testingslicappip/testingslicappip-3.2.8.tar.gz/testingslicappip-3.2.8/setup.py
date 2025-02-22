# -*- coding: utf-8 -*-

import os, shutil
from os.path import expanduser
import setuptools
from setuptools.command.install import install

INSTALLVERSION="3.2.8"

class InstallWrapper(install):
    """
    Provides a install wrapper for SLiCAP.
    Contains private functions that are to be run.
    """
    def run(self):
        """
        Runs the SLiCAP installation.

        Returns
        -------
        None.
        """
        self._set_version_config()
        self._copy_files()
        install.run(self)

    def _set_version_config(self):
        """
        Sets the SLiCAP version variable to be set in the config file
        Can be appended to get the version variable from a website

        Returns
        -------
        None.

        """
        self._SLiCAP_version = INSTALLVERSION
        print("SLiCAP version:", self._SLiCAP_version)

    def _copy_files(self):
        """
        Sets the SLiCAP library variable to be set in the config file
        Includes copying of the default libraries

        Returns
        -------
        None.

        """
        home = expanduser("~")
        slicap_home = os.path.join(home, 'SLiCAP')
        try:
            if os.path.exists(slicap_home):
                shutil.rmtree(slicap_home)
            doc_loc = os.path.join(slicap_home, 'docs')
            shutil.copytree('files/', slicap_home)
            shutil.copytree('docs/_build/html/', doc_loc)
        except:
            print("ERROR: could not copy documentation, styles, and libraries.")


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="testingslicappip",
    version=INSTALLVERSION,
    author="Anton Montagne",
    author_email="anton@montagne.nl",
    description="Symbolic Linear Circuit Analysis Program",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Tim-van-den-Akker/testingslicappip/",
    packages=setuptools.find_packages(),
    cmdclass={'install': InstallWrapper},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.12',
    install_requires=[
    "docutils>=0.18",
    "numpy>=1.26",
    "sympy>=1.12",
    "scipy>=1.12",
    "ply>=3.11",
    "matplotlib>=3.8.0",
    "sphinx-rtd-theme>=1.2.0",
    "svgelements>=1.9.6",
    "cairosvg>=2.7.1",
    "IPython>=8.19",
    'windows_tools>=2.4; sys_platform == "win32"',
    'pywin32>306; sys_platform == "win32"',
],
)
