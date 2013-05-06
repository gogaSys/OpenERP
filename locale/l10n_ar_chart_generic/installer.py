# -*- coding: utf-8 -*-
##############################################################################
#
# Copyright (C) 2012 OpenERP - Team de Localización Argentina.
# https://launchpad.net/~openerp-l10n-ar-localization
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp.osv import fields, osv

class account_modules_ar_installer(osv.osv_memory):
    _name = 'account.modules.ar.installer'
    _inherit = 'res.config.installer'
    _columns = {
        'l10n_ar_invoice': fields.boolean(u'Basic Invoice'),
        'l10n_ar_wsafip_fe': fields.boolean(u'Electronic Invoice'),
        'treasury': fields.boolean(u'Treasury'),
    }

    _defaults= {
        'l10n_ar_invoice': True,
        'l10n_ar_wsafip_fe': True,
        'treasury': True,
    }

account_modules_ar_installer()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
