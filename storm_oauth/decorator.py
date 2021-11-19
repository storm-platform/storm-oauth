#
# This file is part of Access Control module for the Storm platform..
# Copyright (C) 2021 INPE.
#
# Authentication module for the Storm platform. is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

from flask import g

from invenio_access import authenticated_user
from flask_principal import Identity, Need

from bdc_auth_client.decorators import oauth2 as oauth2base


def oauth2access(func, **kwargs):
    """Brazil Data Cube OAuth 2.0 authentication client.

    This decorator validates user entries on the Brazil Data Cube OAuth 2.0 service. After
    validation, a `flask_principal.Identity` is defined to use the Invenio Framework functionality.

    Args:
        func (callable): Decorated function

        kwargs (dict): Parameters passed to `bdc_auth_client.decorators.oauth2`.

    Returns:
        callable: Wrapper function.
    """

    @oauth2base(**kwargs)
    def wrapper(*args, **kwargs):
        # getting user profile
        user_id = kwargs["user_id"]

        # creating the base user identity
        user_profile_identity = Identity(user_id)
        user_profile_identity.provides.add(authenticated_user)
        user_profile_identity.provides.add(Need(method="id", value=user_id))

        # `identity` is used by invenio framework services to validate the permissions
        g.identity = user_profile_identity
        return func(*args, **kwargs)

    return wrapper


__all__ = "oauth2access"
