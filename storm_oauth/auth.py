#
# This file is part of Access Control module for the Storm platform..
# Copyright (C) 2021 INPE.
#
# Authentication module for the Storm platform. is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

from flask import current_app
from flask_login import login_user, logout_user

from flask_principal import (
    AnonymousIdentity,
    identity_changed,
    Identity,
    Need,
)

from functools import partial

from bdc_auth_client.decorators import oauth2 as oauth2base

from .user import UserManager


#
# Login function
#
def oauth2access():
    """Brazil Data Cube OAuth 2.0 authentication client.

    This function validates user entries on the Brazil Data Cube OAuth 2.0 service. After
    validation, a `flask_principal.Identity` is defined to use the Invenio Framework functionality.
    """

    @oauth2base()
    def _authentication(*args, **kwargs):
        # getting user profile
        user_id = kwargs["user_id"]

        user_obj = UserManager.resolve_user(user_id)
        if not user_obj:
            user_obj = UserManager.create_user(user_id)

        # creating the base user identity
        user_identity = Identity(user_id)

        # `system_role` is extracted from `invenio-access` module to reduce library dependencies
        # on this module.
        user_identity.provides.add(partial(Need, "system_role")("authenticated_user"))
        user_identity.provides.add(Need(method="id", value=user_id))

        # setting the user in the identity and the context stack
        login_user(user_obj)
        user_identity.user = user_obj

        # updating the flask-principal request identity
        identity_changed.send(current_app._get_current_object(), identity=user_identity)

    _authentication()


#
# Logout function
#
def oauth2access_logout(error=None):
    """Remove session from flask context."""
    logout_user()
    identity_changed.send(
        current_app._get_current_object(), identity=AnonymousIdentity()
    )


__all__ = ("oauth2access", "oauth2access_logout")
