#
# This file is part of Access Control module for the Storm platform..
# Copyright (C) 2021 INPE.
#
# Authentication module for the Storm platform. is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

from flask_security import UserMixin


class OAuthUser(UserMixin):
    """OAuth user model."""

    def __init__(self, id, email):
        self.id = id
        self.email = email


__all__ = "OAuthUser"
