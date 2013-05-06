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
{
    'name': 'Account Check Debit Note',
    'version': '1.7.155',
    'author': 'OpenERP - Team de Localización Argentina',
    'description': """
    Add the type field to the invoices, allowing to input debit notes
    """,
    'category': 'Generic Modules/Accounting',
    'depends': ["account","account_voucher",
                ],
    'init_xml': [],
    'demo_xml': [],
    'update_xml': [
        'invoice_view.xml',
    ],
    'test': [
    ],
    'active': False,
    'installable': True,
}
