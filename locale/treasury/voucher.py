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

from openerp.osv import osv, fields
from openerp.tools.translate import _

class account_voucher (osv.osv):
    _inherit = 'account.voucher'
    _columns = {
                'treasury_ids' : fields.many2many('account.treasury',
                                'account_voucher_treasury_rel',
                                'voucher_id',
                                'treasury_id',
                                'Associated Treasuries'), 
		}

account_voucher()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
