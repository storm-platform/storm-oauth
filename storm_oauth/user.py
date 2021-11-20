#
# This file is part of Access Control module for the Storm platform..
# Copyright (C) 2021 INPE.
#
# Authentication module for the Storm platform. is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

from flask import current_app

from werkzeug.local import LocalProxy


#
# Flask-Security Datastore
#
datastore = LocalProxy(lambda: current_app.extensions["security"].datastore)


class UserManager:
    @staticmethod
    def resolve_user(user_id: int):
        # search for the user in the datastore
        return datastore.get_user(user_id)

    @staticmethod
    def create_user(user_id: int, email: str = None):
        user_data = datastore.get_user(user_id)

        if not user_data:
            user_data = datastore.create_user(id=user_id, email=email)
            datastore.commit()
        return user_data


__all__ = "UserManager"
