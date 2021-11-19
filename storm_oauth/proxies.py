#
# This file is part of Access Control module for the Storm platform..
# Copyright (C) 2021 INPE.
#
# Authentication module for the Storm platform. is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

from flask import current_app
from werkzeug.local import LocalProxy

current_storm_oauth = LocalProxy(lambda: current_app.extensions["storm-oauth"])
