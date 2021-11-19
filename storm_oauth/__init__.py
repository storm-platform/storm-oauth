#
# This file is part of Access Control module for the Storm platform..
# Copyright (C) 2021 INPE.
#
# Authentication module for the Storm platform. is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

"""Authentication module for the Storm platform.."""

from .decorator import oauth2access

from .version import __version__


__all__ = ("__version__", "oauth2access")
