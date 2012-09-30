#
# gtkui.py
#
# Copyright (C) 2011 Calum Lind <calumlind+deluge@gmail.com>
#
# Basic plugin template created by:
# Copyright (C) 2008 Martijn Voncken <mvoncken@gmail.com>
# Copyright (C) 2007-2009 Andrew Resch <andrewresch@gmail.com>
# Copyright (C) 2009 Damien Churchill <damoxc@gmail.com>
#
# Deluge is free software.
#
# You may redistribute it and/or modify it under the terms of the
# GNU General Public License, as published by the Free Software
# Foundation; either version 3 of the License, or (at your option)
# any later version.
#
# deluge is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with deluge.    If not, write to:
# 	The Free Software Foundation, Inc.,
# 	51 Franklin Street, Fifth Floor
# 	Boston, MA  02110-1301, USA.
#
#    In addition, as a special exception, the copyright holders give
#    permission to link the code of portions of this program with the OpenSSL
#    library.
#    You must obey the GNU General Public License in all respects for all of
#    the code used other than OpenSSL. If you modify file(s) with this
#    exception, you may extend this exception to your version of the file(s),
#    but you are not obligated to do so. If you do not wish to do so, delete
#    this exception statement from your version. If you delete this exception
#    statement from all source files in the program, then also delete it here.
#

import gtk

from deluge.log import LOG as log
from deluge.ui.client import client
from deluge.plugins.pluginbase import GtkPluginBase
import deluge.component as component
import deluge.common

from common import get_resource

class GtkUI(GtkPluginBase):
    def enable(self):
        log.debug("IPstatusbar GtkUI enable..")

        def _on_get_ipaddress(ip_address):
            self.status_item = component.get("StatusBar").add_item(
                text="Ext IP: %s" % ip_address,
                callback=self._on_status_item_clicked,
                tooltip="External IP Address")

        client.ipstatusbar.get_ipaddress().addCallback(_on_get_ipaddress)

    def disable(self):
        # Remove status item
        component.get("StatusBar").remove_item(self.status_item)
        del self.status_item

    def _on_status_item_clicked(self, widget, event):
        self.status_item.set_text("Updating...")
        def _on_get_ipaddress(ip_address):
            self.status_item.set_text("Ext IP: %s" % ip_address)
        client.ipstatusbar.get_ipaddress().addCallback(_on_get_ipaddress)
