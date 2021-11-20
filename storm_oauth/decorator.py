#
# This file is part of Access Control module for the Storm platform..
# Copyright (C) 2021 INPE.
#
# Authentication module for the Storm platform. is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

from flask import current_app, _request_ctx_stack

from flask_principal import (
    identity_changed,
    Identity,
    Need,
)

from functools import partial

from bdc_auth_client.decorators import oauth2 as oauth2base

from .models import OAuthUser


def oauth2access():
    """Brazil Data Cube OAuth 2.0 authentication client.

    This function validates user entries on the Brazil Data Cube OAuth 2.0 service. After
    validation, a `flask_principal.Identity` is defined to use the Invenio Framework functionality.

    Args:
        func (callable): Decorated function

        kwargs (dict): Parameters passed to `bdc_auth_client.decorators.oauth2`.

    Returns:
        callable: Wrapper function.
    """

    @oauth2base()
    def _authentication(*args, **kwargs):
        # getting user profile
        user_id = kwargs["user_id"]
        user_email = kwargs.get("email", None)

        # creating the base user identity
        user_identity = Identity(user_id)

        # `system_role` is extracted from `invenio-access` module to reduce library dependencies
        # on this module.
        user_identity.provides.add(partial(Need, "system_role"))
        user_identity.provides.add(Need(method="id", value=user_id))

        # defining the logged user
        user_obj = OAuthUser(id=user_id, email=user_email)

        # setting the user in the identity and the context stack
        user_identity.user = user_obj
        _request_ctx_stack.top.user = user_obj

        # updating the flask-principal request identity
        identity_changed.send(current_app._get_current_object(), identity=user_identity)

    _authentication()


__all__ = "oauth2access"
