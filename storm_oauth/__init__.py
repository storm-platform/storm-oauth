# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 Storm Project.
#
# storm-oauth is free software; you can redistribute it and/or modify it under
# the terms of the MIT License; see LICENSE file for more details.

"""Authentication module for the Storm platform."""

from .ext import StormOAuth
from .auth import oauth2access, oauth2access_logout

from .version import __version__


__all__ = ("__version__", "StormOAuth", "oauth2access")
