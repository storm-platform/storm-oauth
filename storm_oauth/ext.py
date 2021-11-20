#
# This file is part of Access Control module for the Storm platform..
# Copyright (C) 2021 INPE.
#
# Authentication module for the Storm platform. is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

"""Storm module that adds support for Projects."""

from . import config

from .auth import oauth2access, oauth2access_logout


class StormOAuth(object):
    """storm-oauth extension."""

    def __init__(self, app=None):
        """Extension initialization."""
        if app:
            self.init_app(app)

    def init_app(self, app):
        """Flask application initialization."""
        self.init_config(app)
        self.init_oauth(app)

        app.extensions["storm-oauth"] = self

    def init_config(self, app):
        """Initialize configuration."""
        for k in dir(config):
            if k.startswith("BDC_AUTH_"):
                app.config.setdefault(k, getattr(config, k))

    def init_oauth(self, app):
        """Initialize the Brazil Data Cube OAuth 2.0 client."""

        #
        # Before each request
        #
        app.before_request(oauth2access)

        #
        # After each request (even if it has an exception)
        #
        app.teardown_request(oauth2access_logout)


__all__ = "StormOAuth"
