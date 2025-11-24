# -*- coding: utf-8 -*-
# "Nautilus Open With Menu" 0.8
# Copyright (C) 2018-2023 Romain F. T.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.

import os, gi, gettext, urllib
gi.require_version("Gtk", "4.0")
gi.require_version("Nautilus", "4.1")

from gi.repository import Nautilus, Gtk, GObject, Gio, GLib

class OpenWithMenu(GObject.GObject, Nautilus.MenuProvider):
    """'Open With…' Menu"""

    def __init__(self):
        pass

    def get_file_items_full(self, window, files):
        """Compatible with Nautilus 4.1+"""
        if not files:
            return []
        return self._generate_menu(files)

    def get_background_items(self, *args):
        """Nautilus invokes this function when building the menu on the empty background."""
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
        item = Nautilus.MenuItem(name=item_name, label=item_label, sensitive=True)
        item.connect('activate', self._open_with_app, app)
        return item

    def _open_with_app(self, menuitem, app):
        if app.supports_uris():
            uris = [item.get_uri() for item in self.files]
            app.launch_uris(uris)
        elif app.supports_files():
            files = [item.get_location() for item in self.files]
            app.launch(files)
