..
    This file is part of Access Control module for the Storm platform..
    Copyright (C) 2021 INPE.

    Authentication module for the Storm platform. is free software; you can redistribute it and/or modify it
    under the terms of the MIT License; see LICENSE file for more details.


=============================================
Authentication module for the Storm platform
=============================================


.. image:: https://img.shields.io/badge/license-MIT-green
        :target: https://github.com//storm-platform/storm-access/blob/master/LICENSE
        :alt: Software License

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/psf/black


.. image:: https://img.shields.io/badge/lifecycle-maturing-blue.svg
        :target: https://www.tidyverse.org/lifecycle/#maturing
        :alt: Software Life Cycle

.. image:: https://codecov.io/gh/storm-platform/storm-access/branch/master/graph/badge.svg
        :target: https://codecov.io/gh/storm-platform/storm-access
        :alt: Code Coverage Test

.. image:: https://readthedocs.org/projects/storm_access/badge/?version=latest
        :target: https://storm_access.readthedocs.io/en/latest/
        :alt: Documentation Status

.. image:: https://img.shields.io/github/tag/storm-platform/storm-access.svg
        :target: https://github.com/storm-platform/storm-access/releases
        :alt: Release


.. image:: https://img.shields.io/pypi/v/storm_access
        :target: https://pypi.org/project/storm_access/
        :alt: Python Package Index


.. image:: https://img.shields.io/discord/689541907621085198?logo=discord&logoColor=ffffff&color=7389D8
        :target: https://discord.com/channels/689541907621085198#
        :alt: Join us at Discord


About
=====


A Brazil Data Cube OAuth 2.0 based Client authentication module for the Storm platform.

Features:

- Integration between Brazil Data Cube OAuth 2.0 and `invenio-accounts <https://invenio-accounts.readthedocs.io/en/latest/>`_;
- Internal session control per request (Required for invenio modules) based on `Flask-Login <https://flask-login.readthedocs.io/en/latest/>`_;
- `Flask-Principal <https://pythonhosted.org/Flask-Principal/>`_ integration for useful user identity generation.
