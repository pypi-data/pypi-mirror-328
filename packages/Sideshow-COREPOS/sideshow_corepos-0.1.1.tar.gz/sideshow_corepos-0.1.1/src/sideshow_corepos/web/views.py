# -*- coding: utf-8; -*-
################################################################################
#
#  Sideshow-COREPOS -- Case/Special Order Tracker for CORE-POS
#  Copyright © 2025 Lance Edgar
#
#  This file is part of Sideshow.
#
#  Sideshow is free software: you can redistribute it and/or modify it
#  under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Sideshow is distributed in the hope that it will be useful, but
#  WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#  General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with Sideshow.  If not, see <http://www.gnu.org/licenses/>.
#
################################################################################
"""
Sideshow-COREPOS - custom views

This adds config for readonly views for CORE-POS members and products.
"""


def includeme(config):

    # CORE-POS views
    config.include('wutta_corepos.web.views.corepos.members')
    config.include('wutta_corepos.web.views.corepos.products')
