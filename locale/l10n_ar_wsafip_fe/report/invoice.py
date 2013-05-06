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

import time
from openerp.report import report_sxw
from openerp.addons.l10n_ar_invoice.report.invoice import ar_account_invoice

class fe_account_invoice(ar_account_invoice):

    def _is_electronic(self, o):
        r = True if o.journal_id.afip_authorization_id else False
        return r
    
    def __init__(self, cr, uid, name, context):
        super(fe_account_invoice, self).__init__(cr, uid, name, context=context)
        self.localcontext.update({
            'is_electronic': self._is_electronic,
        })

report_sxw.report_sxw(
    'report.account.invoice_fe',
    'account.invoice',
    'addons/l10n_ar_wsafip_fe/report/invoice.rml',
    parser=fe_account_invoice,
    header=False
)

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
