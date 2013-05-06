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
	"name": "Account Check Duo",
	"version": "1.0",
	"depends": ['account', 'account_voucher','l10n_ar_account_check_debit_note'],
	"author": "OpenERP - Team de Localización Argentina",
	"category": "Generic Modules/Accounting",
	"description": """
    
 This module provides to manage checks (issued and third).
 =========================================================
    Add models of Issued Checks and Third Checks. Add options in Jorunals for using 
    checks in vouchers.    
		""",
	'data': [
			'account_check_duo_view.xml',
            'account_voucher_view.xml',
            'workflow_third.xml',
            'workflow_issued.xml',
            'wizard_third/view_check_deposit.xml',
            'wizard_third/view_check_hreject.xml',
            'wizard_third/view_check_dreject.xml',
            'wizard_third/view_check_sold.xml',
            'wizard_issued/view_issued_check_hreject.xml',
            'partner_view.xml',
            'account_view.xml',
            'security/ir.model.access.csv',
            #'report/report_check_issued.xml',
            #'report/report_check_third.xml',
            ],
            
	'demo': [
	#files containg demo data
	],
	'test': [
	#files containg tests
	 ],
	'installable': True,
	'active': False,
	# 'certificate': '',
}
