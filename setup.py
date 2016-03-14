#!/usr/bin/env python
# ----------------------------------------------------------------------- #
# Copyright 2008-2010, Gregor von Laszewski                               #
# Copyright 2010-2013, Indiana University                                 #
# #
# Licensed under the Apache License, Version 2.0 (the "License"); you may #
# not use this file except in compliance with the License. You may obtain #
# a copy of the License at                                                #
#                                                                         #
# http://www.apache.org/licenses/LICENSE-2.0                              #
#                                                                         #
# Unless required by applicable law or agreed to in writing, software     #
# distributed under the License is distributed on an "AS IS" BASIS,       #
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.#
# See the License for the specific language governing permissions and     #
# limitations under the License.                                          #
# ------------------------------------------------------------------------#
from __future__ import print_function
from setuptools import setup, find_packages
# noinspection PyPep8Naming
from setuptools.command.test import test as TestCommand
from setuptools.command.install import install
import sys
import platform
import os
from cloudmesh_client.util import banner
from cloudmesh_client.setup import os_execute

from cloudmesh_portal.version import __version__

banner("Installing Cloudmesh_portal {:}".format(__version__))

requirements = [
    "cloudmesh_client",
    "cloudmesh_workflow",
    "jinja2schema",
    "django-rest-swagger",
    "django-bootstrap3",
    "django-admin-bootstrapped",
    "django-bootstrap-themes",
    "django-jinja",
    "djangorestframework",
    "markdown",
    "django-filter",
    "aldjemy",
    "nwdiag",
    "pygal"
]


class UploadToPypi(install):
    """Upload the package to pypi. -- only for Maintainers."""

    description = __doc__

    def run(self):
        os.system("make clean")
        commands = """
            python setup.py install
            python setup.py bdist_wheel            
            python setup.py sdist --format=bztar,zip upload
            python setup.py bdist_wheel upload
            """
        os_execute(commands)


class InstallBase(install):
    """Install the cloudmesh_gitissues package."""

    description = __doc__

    def run(self):
        banner("Install readline")
        commands = None
        this_platform = platform.system().lower()
        if this_platform in ['darwin']:
            commands = """
                easy_install readline
                """
        elif this_platform in ['windows']:
            commands = """
                pip install pyreadline
                """
        if commands:
            os_execute(commands)
        banner("Install Cloudmesh_portal {:}".format(__version__))
        install.run(self)


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


home = os.path.expanduser("~")

# home + '/.cloudmesh'
# print [ (home + '/.cloudmesh/' + d, [os.path.join(d, f) for f in files]) for d, folders, files in os.walk('etc')],
# sys.exit()

"""
data_files= [ (os.path.join(home, '.cloudmesh'),
                [os.path.join(d, f) for f in files]) for d, folders, files in os.walk(
                    os.path.join('cloudmesh_client', 'etc'))]
"""

"""
matches = []
for root, dirnames, filenames in os.walk(os.path.join('cloudmesh_client', 'etc')):
  for filename in fnmatch.filter(filenames, '*'):
    matches.append(os.path.join(root, filename).lstrip('cloudmesh_client/'))
data_dirs = matches
"""


# Hack because for some reason requirements does not work
#
# os.system("pip install -r requirements.txt")

class Tox(TestCommand):
    user_options = [('tox-args=', 'a', "Arguments to pass to tox")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.tox_args = None

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import tox
        import shlex
        args = self.tox_args
        if args:
            args = shlex.split(self.tox_args)
        errno = tox.cmdline(args=args)
        sys.exit(errno)


setup(
    version=__version__,
    name="cloudmesh_gitissues",
    description="cloudmesh_gitissues - A portal for cloudmesh"
                "with plugins",
    long_description=read('README.rst'),
    license="Apache License, Version 2.0",
    author="Gregor von Laszewski",
    author_email="laszewski@gmail.com",
    url="https://github.com/cloudmesh/cloudmesh_gitissues",
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 2.7",
        "Topic :: Scientific/Engineering",
        "Topic :: System :: Clustering",
        "Topic :: System :: Distributed Computing",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Environment :: Console"
    ],
    keywords="cloud cmd commandshell plugins",
    packages=find_packages(),
    install_requires=requirements,
    # include_package_data=True,
    # data_files= data_files,
    # package_data={'cloudmesh_gitissues': data_dirs},
    # entry_points={
    #    'console_scripts': [
    #        'issues = cloudmesh_client.shell.issues:main',
    #        'ghost = cloudmesh_client.shell.ghost:main',
    #
    #    ],
    # },
    tests_require=['tox'],
    cmdclass={
        'install': InstallBase,
        'pypi': UploadToPypi,
        'test': Tox,
    },
    dependency_links=[]
)
