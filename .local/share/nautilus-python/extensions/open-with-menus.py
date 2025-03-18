# -*- coding: utf-8 -*-
# "Nautilus Open With Menu" 0.8
# Copyright (C) 2018-2023 Romain F. T.
#
# "Nautilus Open With Menu" is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
# 
# "Nautilus Open With Menu" is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with "Create .desktop file"; if not, see http://www.gnu.org/licenses
# for more information.

import os, gi, gettext, urllib
try:
	gi.require_version("Nautilus", "4.0")
except ValueError:
	gi.require_version("Nautilus", "3.0")
from gi.repository import Nautilus, Gtk, GObject, Gio, GLib

# TODO translations

class OpenWithMenu(GObject.GObject, Nautilus.MenuProvider):
    """'Open With…' Menu"""
    def __init__(self):
        pass

    def get_file_items(self, *args):
        """Nautilus invokes this function when building the menu on files."""
        file_items = args[-1]
        if not len(file_items):
            return
        return self._generate_menu(file_items)

    def get_background_items(self, *args):
        """Nautilus invokes this function when building the menu on the empty
        background."""
        pass

    ############################################################################

    def _generate_menu(self, file_items):
        """Generate the menu items directly under the context menu, with a limit."""
        possible_apps = []
        self.files = file_items

        for item in file_items:
            item_type = item.get_mime_type()
            if len(possible_apps) == 0:
                possible_apps = Gio.AppInfo.get_all_for_type(item_type)
            else:
                possible_apps_new = Gio.AppInfo.get_all_for_type(item_type)
                possible_apps_common = []
                for app in possible_apps:
                    for app2 in possible_apps_new:
                        if app.equal(app2):
                            possible_apps_common.append(app)
                possible_apps = possible_apps_common

        # Limit the number of apps displayed in the context menu
        MAX_ITEMS = 5  # You can change this number to adjust the limit
        menuitems = []

        for i, app in enumerate(possible_apps):
            if i < MAX_ITEMS:
                menuitems.append(self._add_app_item(app, i))
            else:
                break

        return menuitems

    def _add_app_item(self, app, index):
        item_label = app.get_name()
        item_name = 'OpenWithMenu' + str(index)
        # according to the documentation, the constructor has an 'icon'
        # parameter but i don't understand how it works
        item = Nautilus.MenuItem(name=item_name, label=item_label, sensitive=True)
        item.connect('activate', self._open_with_app, app)
        return item

    def _open_with_app(self, menuitem, app):
        if app.supports_uris():
            uris = []
            for item in self.files:
                uris.append(item.get_uri())
            app.launch_uris(uris)
        elif app.supports_files():
            files = []
            for item in self.files:
                files.append(item.get_location())
            app.launch(files)

    ############################################################################

