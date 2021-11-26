#
# This file is part of Access Control module for the Storm platform..
# Copyright (C) 2021 INPE.
#
# Authentication module for the Storm platform. is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

"""Authentication module for the Storm platform."""

import os

from setuptools import find_packages, setup

readme = open("README.rst").read()

history = open("CHANGES.rst").read()

docs_require = [
    "Sphinx>=2.2",
    "sphinx_rtd_theme",
    "sphinx-copybutton",
]

tests_require = [
    "coverage>=4.5",
    "coveralls>=1.8",
    "pytest>=5.2",
    "pytest-cov>=2.8",
    "pytest-pep8>=1.0",
    "pydocstyle>=4.0",
    "isort>4.3",
    "check-manifest>=0.40",
]

examples_require = []

extras_require = {
    "docs": docs_require,
    "examples": examples_require,
    "tests": tests_require,
}

extras_require["all"] = [req for _, reqs in extras_require.items() for req in reqs]

setup_requires = [
    "pytest-runner>=5.2",
]

install_requires = [
    "Click>=7.0",
    # Flask dependencies
    "Flask-Security>=3.0.0",
    "Flask-Principal>=0.4.0",
    "Werkzeug>=2.0.2",
    # Brazil Data Cube Dependencies
    "bdc-auth-client @ git+https://github.com/brazil-data-cube/bdc-auth-client@v0.2.3",
]

packages = find_packages()

g = {}
with open(os.path.join("storm_oauth", "version.py"), "rt") as fp:
    exec(fp.read(), g)
    version = g["__version__"]

setup(
    name="storm_oauth",
    version=version,
    description=__doc__,
    long_description=readme + "\n\n" + history,
    long_description_content_type="text/x-rst",
    keywords=["OAuth 2.0", "Brazil Data Cube", "Authentication"],
    license="MIT",
    author="Felipe Menino Carlos",
    author_email="felipe.carlos@inpe.br",
    url="https://github.com/storm-platform/storm-oauth",
    project_urls={
        "Repository": "https://github.com/storm-platform/storm-oauth",
        "Issues": "https://github.com/storm-platform/storm-oauth/issues",
        "Documentation": "https://storm-oauth.readthedocs.io/en/latest/",
    },
    packages=packages,
    zip_safe=False,
    include_package_data=True,
    platforms="any",
    entry_points={
        "invenio_config.module": [
            "storm_oauth = storm_oauth.config",
        ],
        "invenio_base.api_apps": [
            "storm_oauth = storm_oauth:StormOAuth",
        ],
    },
    extras_require=extras_require,
    install_requires=install_requires,
    setup_requires=setup_requires,
    tests_require=tests_require,
    classifiers=[
        "Development Status :: 1 - Planning",
        "Environment :: Web Environment",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.7",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Scientific/Engineering :: GIS",
    ],
)
